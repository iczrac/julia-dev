"""文档资产可执行契约套件（生成物，勿手改）。"""

import unittest
from pathlib import Path

from src.contracts.doc_gov import contract_check as check_doc_gov
from src.contracts.doc_gov import contract_check as check_doc_gov
from src.contracts.doc_gov import contract_check as check_doc_gov
from src.contracts.doc_req import contract_check as check_doc_req
from src.contracts.doc_arch import contract_check as check_doc_arch
from src.contracts.doc_eng import contract_check as check_doc_eng
from src.contracts.doc_qa import contract_check as check_doc_qa
from src.contracts.doc_rev import contract_check as check_doc_rev
from src.contracts.doc_dsg import contract_check as check_doc_dsg
from src.contracts.doc_kms import contract_check as check_doc_kms
from src.contracts.doc_rel import contract_check as check_doc_rel
from src.contracts.doc_agentfriendlycli import contract_check as check_doc_agentfriendlycli
from src.contracts.doc_codebasereverse import contract_check as check_doc_codebasereverse
from src.contracts.doc_consultinghtmlppt import contract_check as check_doc_consultinghtmlppt
from src.contracts.doc_decisiongates import contract_check as check_doc_decisiongates
from src.contracts.doc_deepdiffreview import contract_check as check_doc_deepdiffreview
from src.contracts.doc_ledgerbridge import contract_check as check_doc_ledgerbridge
from src.contracts.doc_llmknowledgebase import contract_check as check_doc_llmknowledgebase
from src.contracts.doc_okfconsume import contract_check as check_doc_okfconsume
from src.contracts.doc_okfformat import contract_check as check_doc_okfformat
from src.contracts.doc_okfgenerate import contract_check as check_doc_okfgenerate
from src.contracts.doc_ontologydrivendev import contract_check as check_doc_ontologydrivendev
from src.contracts.doc_ontologymodeling import contract_check as check_doc_ontologymodeling
from src.contracts.doc_pstackparallelreview import contract_check as check_doc_pstackparallelreview
from src.contracts.doc_pstackplaybooks import contract_check as check_doc_pstackplaybooks
from src.contracts.doc_pstackprinciples import contract_check as check_doc_pstackprinciples
from src.contracts.doc_pstackverification import contract_check as check_doc_pstackverification
from src.contracts.doc_selfevolution import contract_check as check_doc_selfevolution
from src.contracts.doc_structuredorchestration import contract_check as check_doc_structuredorchestration
from src.contracts.doc_visualmodel import contract_check as check_doc_visualmodel
from src.contracts.doc_dist import contract_check as check_doc_dist

ROOT = Path(__file__).resolve().parent.parent

class DocContractTest(unittest.TestCase):
    def test_doc_gov(self):
        check_doc_gov(ROOT)

    def test_doc_gov(self):
        check_doc_gov(ROOT)

    def test_doc_gov(self):
        check_doc_gov(ROOT)

    def test_doc_req(self):
        check_doc_req(ROOT)

    def test_doc_arch(self):
        check_doc_arch(ROOT)

    def test_doc_eng(self):
        check_doc_eng(ROOT)

    def test_doc_qa(self):
        check_doc_qa(ROOT)

    def test_doc_rev(self):
        check_doc_rev(ROOT)

    def test_doc_dsg(self):
        check_doc_dsg(ROOT)

    def test_doc_kms(self):
        check_doc_kms(ROOT)

    def test_doc_rel(self):
        check_doc_rel(ROOT)

    def test_doc_agentfriendlycli(self):
        check_doc_agentfriendlycli(ROOT)

    def test_doc_codebasereverse(self):
        check_doc_codebasereverse(ROOT)

    def test_doc_consultinghtmlppt(self):
        check_doc_consultinghtmlppt(ROOT)

    def test_doc_decisiongates(self):
        check_doc_decisiongates(ROOT)

    def test_doc_deepdiffreview(self):
        check_doc_deepdiffreview(ROOT)

    def test_doc_ledgerbridge(self):
        check_doc_ledgerbridge(ROOT)

    def test_doc_llmknowledgebase(self):
        check_doc_llmknowledgebase(ROOT)

    def test_doc_okfconsume(self):
        check_doc_okfconsume(ROOT)

    def test_doc_okfformat(self):
        check_doc_okfformat(ROOT)

    def test_doc_okfgenerate(self):
        check_doc_okfgenerate(ROOT)

    def test_doc_ontologydrivendev(self):
        check_doc_ontologydrivendev(ROOT)

    def test_doc_ontologymodeling(self):
        check_doc_ontologymodeling(ROOT)

    def test_doc_pstackparallelreview(self):
        check_doc_pstackparallelreview(ROOT)

    def test_doc_pstackplaybooks(self):
        check_doc_pstackplaybooks(ROOT)

    def test_doc_pstackprinciples(self):
        check_doc_pstackprinciples(ROOT)

    def test_doc_pstackverification(self):
        check_doc_pstackverification(ROOT)

    def test_doc_selfevolution(self):
        check_doc_selfevolution(ROOT)

    def test_doc_structuredorchestration(self):
        check_doc_structuredorchestration(ROOT)

    def test_doc_visualmodel(self):
        check_doc_visualmodel(ROOT)

    def test_doc_dist(self):
        check_doc_dist(ROOT)


if __name__ == "__main__":
    unittest.main()
