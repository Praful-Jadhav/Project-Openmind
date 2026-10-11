import unittest
from scripts.verify_openmind_evidence import material, validate_packet
PACKET = """# Openmind Evidence Packet

Task ID: OM-ZTG-001
Status: IN_PROGRESS
Accountable owner: Openmind maintainer
Risk tier: R2

## Claim and risk
Add evidence gating for material provider-registry code.

## Scope and acceptance criteria
Source, tests, package metadata, workflow changes and public README claims require a source-controlled packet before acceptance.

## Verification plan and results
The workflow runs the gate's unit tests, packet validation, registry unit tests and TypeScript typecheck against the candidate revision.

## Validation plan and results
The intended behavior must be exercised through the registry API and provider adapter contract. This gate itself does not certify production use.

## Security and privacy
No credentials or private ecosystem details belong in source examples, packets or logs.

## Limitations and open items
The checker validates evidence structure only. Runtime authorization, abuse controls and recovery remain separate acceptance items.

## Recovery and rollback
Revert the evidence gate and workflow if a valid packet is rejected or a material change is missed.

## Evidence and tested revision
The exact candidate SHA and CI output will be read back after the workflow completes. No release acceptance is claimed.
"""

class OpenmindEvidenceTests(unittest.TestCase):
    def test_material_paths(self):
        self.assertTrue(material("src/connection-registry.ts"))
        self.assertTrue(material("tests/connection-registry.test.ts"))
        self.assertFalse(material("LICENSE"))
    def test_packet_passes_as_in_progress(self):
        self.assertEqual(validate_packet(PACKET), [])
    def test_missing_section_fails(self):
        text=PACKET.replace("## Security and privacy\nNo credentials or private ecosystem details belong in source examples, packets or logs.\n","")
        self.assertTrue(any("missing section" in e for e in validate_packet(text)))
    def test_accepted_without_readback_fails(self):
        text=PACKET.replace("Status: IN_PROGRESS","Status: ACCEPTED")
        self.assertTrue(any("Independent read-back: PASS" in e for e in validate_packet(text)))
    def test_placeholder_fails(self):
        text=PACKET.replace("Revert the evidence gate and workflow if a valid packet is rejected or a material change is missed.","TODO")
        self.assertTrue(any("placeholder" in e for e in validate_packet(text)))
if __name__=="__main__": unittest.main()
