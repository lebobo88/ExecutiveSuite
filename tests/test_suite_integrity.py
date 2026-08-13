#!/usr/bin/env python3
"""
test_suite_integrity.py — Complete Verification & Invariant Regression Suite
Verifies 100% correctness of frontmatter, tool scoping, XML tags, path references,
and constitutional immutability across ExecutiveSuite.
"""

import hashlib
import json
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PLUGIN_ROOT = REPO_ROOT / "plugins" / "executive-suite"
AGENTS_DIR = PLUGIN_ROOT / "agents"
COMMANDS_DIR = PLUGIN_ROOT / "commands"
SKILLS_DIR = PLUGIN_ROOT / "skills"


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Simple parser for YAML frontmatter in Markdown files."""
    if not content.startswith("---"):
        return {}, content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content
    yaml_str = parts[1].strip()
    body = parts[2].strip()

    data = {}
    current_key = None
    list_accumulator = None

    for line in yaml_str.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("- ") and current_key is not None:
            if list_accumulator is None:
                list_accumulator = []
            list_accumulator.append(line[2:].strip().strip('"').strip("'"))
            data[current_key] = list_accumulator
            continue

        if ":" in line:
            if current_key and list_accumulator is not None:
                data[current_key] = list_accumulator
                list_accumulator = None
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            current_key = key
            if not val:
                list_accumulator = []
                data[key] = list_accumulator
            else:
                if val.lower() == "true":
                    data[key] = True
                elif val.lower() == "false":
                    data[key] = False
                elif val.isdigit():
                    data[key] = int(val)
                else:
                    data[key] = val

    if current_key and list_accumulator is not None:
        data[current_key] = list_accumulator

    return data, body


class TestConstitutionAndGovernance(unittest.TestCase):

    def test_constitution_immutability(self):
        """CONSTITUTION.md SHA-256 hash must match the immortal head."""
        const_path = REPO_ROOT / "CONSTITUTION.md"
        self.assertTrue(const_path.exists(), "CONSTITUTION.md missing")
        content = const_path.read_bytes()
        sha256 = hashlib.sha256(content).hexdigest().upper()
        expected_sha = "339AC010BD91B93CBE5246131648A704CFDB9D6D18E894CAE43DF50F2C5B26EA"
        self.assertEqual(sha256, expected_sha, "CONSTITUTION.md was modified! Constitutional breach.")

    def test_settings_deny_constitution(self):
        """settings.json must contain explicit deny rules protecting CONSTITUTION.md."""
        settings_path = REPO_ROOT / ".claude" / "settings.json"
        self.assertTrue(settings_path.exists(), ".claude/settings.json missing")
        data = json.loads(settings_path.read_text(encoding="utf-8"))
        deny_rules = data.get("permissions", {}).get("deny", [])
        self.assertTrue(any("CONSTITUTION.md" in rule for rule in deny_rules), "Missing CONSTITUTION.md deny rule in settings.json")


class TestPluginManifest(unittest.TestCase):

    def test_plugin_json_schema(self):
        """plugin.json must be valid and contain required and standard metadata fields."""
        manifest_path = PLUGIN_ROOT / ".claude-plugin" / "plugin.json"
        self.assertTrue(manifest_path.exists(), "plugin.json missing")
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
        self.assertEqual(data.get("name"), "executive-suite")
        self.assertIn("version", data)
        self.assertIn("description", data)
        self.assertIn("author", data)
        self.assertIn("license", data)


class TestAgentsIntegrity(unittest.TestCase):

    EXPECTED_AGENTS = {
        "ceo", "cso", "coo", "cfo", "cro", "chief-risk-officer",
        "cto", "cio", "cdo", "caio", "ciso", "cpo", "cmo", "cxo",
        "chief-communications-officer", "chro", "clo", "chief-compliance-officer",
        "csco", "chief-sustainability-officer",
        "boardroom", "mna-cockpit", "crisis-warroom", "capital-allocation"
    }

    ORCHESTRATORS = {"boardroom", "mna-cockpit", "crisis-warroom", "capital-allocation"}

    def test_all_agents_present(self):
        agent_files = {p.stem for p in AGENTS_DIR.glob("*.md")}
        self.assertEqual(agent_files, self.EXPECTED_AGENTS)

    def test_agent_frontmatter_and_prompt_structure(self):
        for agent_file in AGENTS_DIR.glob("*.md"):
            name = agent_file.stem
            content = agent_file.read_text(encoding="utf-8")
            fm, body = parse_frontmatter(content)

            self.assertEqual(fm.get("name"), name, f"Agent {name} name mismatch in frontmatter")
            self.assertIn("description", fm, f"Agent {name} missing description")
            self.assertIn(fm.get("model"), ["opus", "sonnet"], f"Agent {name} model must be opus or sonnet")
            self.assertIsInstance(fm.get("maxTurns"), int, f"Agent {name} maxTurns must be int")
            self.assertIn("color", fm, f"Agent {name} missing color")

            # Tools least-privilege verification
            tools = fm.get("tools", [])
            self.assertIsInstance(tools, list, f"Agent {name} tools must be a list")
            self.assertNotIn("Skill", tools, f"Agent {name} should not have Skill in tools (use skills field)")
            self.assertNotIn("Agent", tools, f"Agent {name} should not have Agent in tools")

            # Skills resolution
            skills = fm.get("skills", [])
            self.assertIsInstance(skills, list, f"Agent {name} skills must be a list")
            for sk in skills:
                skill_path = SKILLS_DIR / sk / "SKILL.md"
                self.assertTrue(skill_path.exists(), f"Agent {name} references non-existent skill: {sk}")

            # Orchestrator-specific checks
            if name in self.ORCHESTRATORS:
                self.assertEqual(fm.get("effort"), "high", f"Orchestrator {name} must have effort: high")
                self.assertIn("You do NOT spawn subagents", body, f"Orchestrator {name} missing no-spawn declaration")
                has_workflow_or_debate = any(tag in body for tag in ["<workflow>", "<debate_protocol>", "<workflow_6_steps>", "<workflow_7_steps>"])
                self.assertTrue(has_workflow_or_debate, f"Orchestrator {name} missing workflow/protocol tag")
            else:
                self.assertIn("<decision_framework>", body, f"Single-domain agent {name} missing <decision_framework>")

            # XML tags hierarchy checks
            self.assertIn("<trusted_policy>", body, f"Agent {name} missing <trusted_policy>")
            self.assertIn("CONSTITUTION.md is immutable", body, f"Agent {name} missing CONSTITUTION rule in policy")
            self.assertIn("Never bypass HITL", body, f"Agent {name} missing HITL rule in policy")
            self.assertIn("<role_definition>", body, f"Agent {name} missing <role_definition>")
            self.assertIn("<evidence_and_uncertainty>", body, f"Agent {name} missing <evidence_and_uncertainty>")
            self.assertIn("Information not specified", body, f"Agent {name} missing uncertainty authorization")
            self.assertIn("<constraints>", body, f"Agent {name} missing <constraints>")
            self.assertIn("<output_contract>", body, f"Agent {name} missing <output_contract>")


class TestCommandsIntegrity(unittest.TestCase):

    EXPECTED_COMMANDS = {
        "board-meeting", "capital-decision", "crisis-mode", "decision-memo",
        "exec-brief", "executive-team", "mna-review", "quarterly-review", "risk-stress"
    }

    HEAVY_COMMANDS = {"board-meeting", "capital-decision", "crisis-mode", "mna-review", "quarterly-review", "risk-stress"}

    def test_all_commands_present(self):
        cmd_files = {p.stem for p in COMMANDS_DIR.glob("*.md")}
        self.assertEqual(cmd_files, self.EXPECTED_COMMANDS)

    def test_command_frontmatter_and_arguments(self):
        for cmd_file in COMMANDS_DIR.glob("*.md"):
            name = cmd_file.stem
            content = cmd_file.read_text(encoding="utf-8")
            fm, body = parse_frontmatter(content)

            self.assertIn("description", fm, f"Command {name} missing description")
            self.assertIn("argument-hint", fm, f"Command {name} missing argument-hint")

            if name in self.HEAVY_COMMANDS:
                self.assertTrue(fm.get("disable-model-invocation"), f"Heavy command {name} must have disable-model-invocation: true")

            # Check that input placeholder $ARGUMENTS is present in body
            if name != "executive-team":
                self.assertIn("$ARGUMENTS", body, f"Command {name} missing $ARGUMENTS placeholder")

            # Check for zero broken .claude/ path references
            self.assertNotIn(".claude/agents/", body, f"Command {name} has stale .claude/agents/ path reference")
            self.assertNotIn(".claude/commands/", body, f"Command {name} has stale .claude/commands/ path reference")
            self.assertNotIn(".claude/skills/", body, f"Command {name} has stale .claude/skills/ path reference")


class TestSkillsIntegrity(unittest.TestCase):

    EXPECTED_SKILLS = {
        "ai-governance", "crisis-response", "debate-protocol", "enterprise-risk",
        "executive-protocol", "financial-frameworks", "mna-playbook",
        "scenario-planning", "stakeholder-comms"
    }

    REFERENCE_SKILLS = {"crisis-response", "debate-protocol", "enterprise-risk", "mna-playbook", "scenario-planning", "stakeholder-comms"}

    def test_all_skills_present(self):
        skill_dirs = {p.name for p in SKILLS_DIR.iterdir() if p.is_dir()}
        self.assertEqual(skill_dirs, self.EXPECTED_SKILLS)

    def test_skill_frontmatter(self):
        for skill_name in self.EXPECTED_SKILLS:
            skill_file = SKILLS_DIR / skill_name / "SKILL.md"
            self.assertTrue(skill_file.exists(), f"SKILL.md missing for {skill_name}")
            content = skill_file.read_text(encoding="utf-8")
            fm, body = parse_frontmatter(content)

            self.assertEqual(fm.get("name"), skill_name, f"Skill {skill_name} name mismatch in frontmatter")
            self.assertIn("description", fm, f"Skill {skill_name} missing description")
            self.assertIn("allowed-tools", fm, f"Skill {skill_name} missing allowed-tools")

            tools = fm.get("allowed-tools", [])
            self.assertIsInstance(tools, list, f"Skill {skill_name} allowed-tools must be list")

            if skill_name in self.REFERENCE_SKILLS:
                self.assertNotIn("Write", tools, f"Reference-only skill {skill_name} should not have Write in allowed-tools")


if __name__ == "__main__":
    unittest.main()
