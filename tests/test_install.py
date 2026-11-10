#!/usr/bin/env python3
"""Test unitari di install.py (nessuna dipendenza esterna).

Verificano copia, collegamento, sovrascrittura, dry-run e disinstallazione su
directory temporanee. Non verificano il comportamento dei client agentici.
"""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import install  # noqa: E402


class InstallTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.target = Path(self.tmp.name) / "skills"
        self.skill = install.skill_dirs()[0]

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_skill_dirs_sono_cartelle_con_skill_md(self) -> None:
        skills = install.skill_dirs()
        self.assertGreaterEqual(len(skills), 10)
        for skill in skills:
            self.assertTrue((skill / "SKILL.md").is_file())
            self.assertTrue(skill.name.startswith("eu-funding-"))

    def test_presets_contengono_i_client_principali(self) -> None:
        presets = install.presets()
        for name in ("claude", "claude-project", "opencode", "opencode-project"):
            self.assertIn(name, presets)
        self.assertEqual(presets["claude"].name, "skills")
        self.assertEqual(presets["opencode"].parent.name, "opencode")

    def test_same_tree_confronta_il_contenuto(self) -> None:
        self.assertTrue(install.same_tree(self.skill, self.skill))
        with tempfile.TemporaryDirectory() as other:
            copy = Path(other) / self.skill.name
            install.install_one(self.skill, Path(other), False, False)
            self.assertTrue(install.same_tree(self.skill, copy))
            (copy / "SKILL.md").write_text("diverso", encoding="utf-8")
            self.assertFalse(install.same_tree(self.skill, copy))

    def test_same_tree_ignora_artefatti_locali(self) -> None:
        with tempfile.TemporaryDirectory() as other:
            copy = Path(other) / self.skill.name
            install.install_one(self.skill, Path(other), False, False)
            (copy / "__pycache__").mkdir()
            (copy / "__pycache__" / "x.pyc").write_bytes(b"cache")
            (copy / ".DS_Store").write_bytes(b"junk")
            self.assertTrue(install.same_tree(self.skill, copy))

    def test_copia_e_reinstallazione_idempotente(self) -> None:
        self.assertEqual(install.install_one(self.skill, self.target, False, False), "copiata")
        self.assertTrue((self.target / self.skill.name / "SKILL.md").is_file())
        self.assertEqual(
            install.install_one(self.skill, self.target, False, False),
            "già installata (identica)",
        )

    def test_versione_diversa_richiede_force(self) -> None:
        install.install_one(self.skill, self.target, False, False)
        (self.target / self.skill.name / "SKILL.md").write_text("x", encoding="utf-8")
        self.assertIn("saltata", install.install_one(self.skill, self.target, False, False))
        self.assertEqual(install.install_one(self.skill, self.target, False, True), "copiata")
        self.assertTrue(install.same_tree(self.skill, self.target / self.skill.name))

    def test_collegamento(self) -> None:
        self.assertEqual(install.install_one(self.skill, self.target, True, False), "collegata")
        dest = self.target / self.skill.name
        self.assertTrue(dest.is_symlink())
        self.assertEqual(dest.resolve(), self.skill.resolve())
        self.assertEqual(
            install.install_one(self.skill, self.target, True, False),
            "già installata (collegamento)",
        )

    def test_dry_run_non_modifica(self) -> None:
        self.assertEqual(
            install.install_one(self.skill, self.target, False, False, True), "copierebbe"
        )
        self.assertFalse(self.target.exists())
        self.assertEqual(install.main([str(self.target), "--dry-run"]), 0)
        self.assertFalse(self.target.exists())

    def test_disinstallazione(self) -> None:
        install.install_one(self.skill, self.target, False, False)
        self.assertEqual(install.uninstall_one(self.skill, self.target), "rimossa")
        self.assertFalse((self.target / self.skill.name).exists())
        self.assertEqual(install.uninstall_one(self.skill, self.target), "non presente")

    def test_disinstallazione_non_tocca_cartelle_estranee(self) -> None:
        estranea = self.target / self.skill.name
        estranea.mkdir(parents=True)
        (estranea / "note.txt").write_text("mia", encoding="utf-8")
        self.assertIn("saltata", install.uninstall_one(self.skill, self.target))
        self.assertTrue((estranea / "note.txt").is_file())

    def test_percorso_inesistente_viene_creato(self) -> None:
        self.assertEqual(install.main([str(self.target)]), 0)
        self.assertEqual(len(list(self.target.iterdir())), len(install.skill_dirs()))


if __name__ == "__main__":
    unittest.main(verbosity=2)
