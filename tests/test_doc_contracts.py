"""文档资产可执行契约套件（生成物，勿手改）。"""

import unittest
from pathlib import Path

from src.contracts.doc_gov_01 import contract_check as check_doc_gov_01
from src.contracts.doc_gov_02 import contract_check as check_doc_gov_02
from src.contracts.doc_gov_03 import contract_check as check_doc_gov_03
from src.contracts.doc_req_04 import contract_check as check_doc_req_04
from src.contracts.doc_arch_05 import contract_check as check_doc_arch_05
from src.contracts.doc_eng_06 import contract_check as check_doc_eng_06
from src.contracts.doc_qa_07 import contract_check as check_doc_qa_07
from src.contracts.doc_rev_08 import contract_check as check_doc_rev_08
from src.contracts.doc_dsg_09 import contract_check as check_doc_dsg_09
from src.contracts.doc_kms_10 import contract_check as check_doc_kms_10
from src.contracts.doc_rel_11 import contract_check as check_doc_rel_11
from src.contracts.doc_agentfriendlycli_01 import contract_check as check_doc_agentfriendlycli_01
from src.contracts.doc_codebasereverse_02 import contract_check as check_doc_codebasereverse_02
from src.contracts.doc_consultinghtmlppt_03 import contract_check as check_doc_consultinghtmlppt_03
from src.contracts.doc_decisiongates_04 import contract_check as check_doc_decisiongates_04
from src.contracts.doc_deepdiffreview_05 import contract_check as check_doc_deepdiffreview_05
from src.contracts.doc_ledgerbridge_06 import contract_check as check_doc_ledgerbridge_06
from src.contracts.doc_llmknowledgebase_07 import contract_check as check_doc_llmknowledgebase_07
from src.contracts.doc_okfconsume_08 import contract_check as check_doc_okfconsume_08
from src.contracts.doc_okfformat_09 import contract_check as check_doc_okfformat_09
from src.contracts.doc_okfgenerate_10 import contract_check as check_doc_okfgenerate_10
from src.contracts.doc_ontologydrivendev_11 import contract_check as check_doc_ontologydrivendev_11
from src.contracts.doc_ontologymodeling_12 import contract_check as check_doc_ontologymodeling_12
from src.contracts.doc_pstackparallelreview_13 import contract_check as check_doc_pstackparallelreview_13
from src.contracts.doc_pstackplaybooks_14 import contract_check as check_doc_pstackplaybooks_14
from src.contracts.doc_pstackprinciples_15 import contract_check as check_doc_pstackprinciples_15
from src.contracts.doc_pstackverification_16 import contract_check as check_doc_pstackverification_16
from src.contracts.doc_selfevolution_17 import contract_check as check_doc_selfevolution_17
from src.contracts.doc_structuredorchestration_18 import contract_check as check_doc_structuredorchestration_18
from src.contracts.doc_visualmodel_19 import contract_check as check_doc_visualmodel_19
from src.contracts.doc_dist import contract_check as check_doc_dist

ROOT = Path(__file__).resolve().parent.parent

class DocContractTest(unittest.TestCase):
    def test_doc_gov_01(self):
        check_doc_gov_01(ROOT)

    def test_doc_gov_02(self):
        check_doc_gov_02(ROOT)

    def test_doc_gov_03(self):
        check_doc_gov_03(ROOT)

    def test_doc_req_04(self):
        check_doc_req_04(ROOT)

    def test_doc_arch_05(self):
        check_doc_arch_05(ROOT)

    def test_doc_eng_06(self):
        check_doc_eng_06(ROOT)

    def test_doc_qa_07(self):
        check_doc_qa_07(ROOT)

    def test_doc_rev_08(self):
        check_doc_rev_08(ROOT)

    def test_doc_dsg_09(self):
        check_doc_dsg_09(ROOT)

    def test_doc_kms_10(self):
        check_doc_kms_10(ROOT)

    def test_doc_rel_11(self):
        check_doc_rel_11(ROOT)

    def test_doc_agentfriendlycli_01(self):
        check_doc_agentfriendlycli_01(ROOT)

    def test_doc_codebasereverse_02(self):
        check_doc_codebasereverse_02(ROOT)

    def test_doc_consultinghtmlppt_03(self):
        check_doc_consultinghtmlppt_03(ROOT)

    def test_doc_decisiongates_04(self):
        check_doc_decisiongates_04(ROOT)

    def test_doc_deepdiffreview_05(self):
        check_doc_deepdiffreview_05(ROOT)

    def test_doc_ledgerbridge_06(self):
        check_doc_ledgerbridge_06(ROOT)

    def test_doc_llmknowledgebase_07(self):
        check_doc_llmknowledgebase_07(ROOT)

    def test_doc_okfconsume_08(self):
        check_doc_okfconsume_08(ROOT)

    def test_doc_okfformat_09(self):
        check_doc_okfformat_09(ROOT)

    def test_doc_okfgenerate_10(self):
        check_doc_okfgenerate_10(ROOT)

    def test_doc_ontologydrivendev_11(self):
        check_doc_ontologydrivendev_11(ROOT)

    def test_doc_ontologymodeling_12(self):
        check_doc_ontologymodeling_12(ROOT)

    def test_doc_pstackparallelreview_13(self):
        check_doc_pstackparallelreview_13(ROOT)

    def test_doc_pstackplaybooks_14(self):
        check_doc_pstackplaybooks_14(ROOT)

    def test_doc_pstackprinciples_15(self):
        check_doc_pstackprinciples_15(ROOT)

    def test_doc_pstackverification_16(self):
        check_doc_pstackverification_16(ROOT)

    def test_doc_selfevolution_17(self):
        check_doc_selfevolution_17(ROOT)

    def test_doc_structuredorchestration_18(self):
        check_doc_structuredorchestration_18(ROOT)

    def test_doc_visualmodel_19(self):
        check_doc_visualmodel_19(ROOT)


if __name__ == "__main__":
    unittest.main()
