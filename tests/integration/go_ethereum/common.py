import pytest

from web3._utils.module_testing import (  # noqa: F401
    EthModuleTest,
    GoEthereumAdminModuleTest,
    GoEthereumPersonalModuleTest,
    GoEthereumShhModuleTest,
    NetModuleTest,
    VersionModuleTest,
    Web3ModuleTest,
)


class GoEthereumTest(Web3ModuleTest):
    def _check_web3_clientVersion(self, client_version):
        assert client_version.startswith('Geth/')


class GoEthereumEthModuleTest(EthModuleTest):
    def test_eth_replaceTransaction_already_mined(self, web3, unlocked_account_dual_type):
        web3.geth.miner.start()
        super().test_eth_replaceTransaction_already_mined(web3, unlocked_account_dual_type)
        web3.geth.miner.stop()

    @pytest.mark.xfail(reason='Block identifier has not been implemented in geth')
    def test_eth_estimateGas_with_block(self,
                                        web3,
                                        unlocked_account_dual_type):
        super().test_eth_estimateGas_with_block(
            web3, unlocked_account_dual_type
        )

    @pytest.mark.xfail(reason='eth_signTypedData has not been released in geth')
    def test_eth_signTypedData(self,
                               web3,
                               unlocked_account_dual_type):
        super().test_eth_signTypedData(
            web3, unlocked_account_dual_type
        )

    @pytest.mark.xfail(reason='eth_signTypedData has not been released in geth')
    def test_invalid_eth_signTypedData(self,
                                       web3,
                                       unlocked_account_dual_type):
        super().test_invalid_eth_signTypedData(
            web3, unlocked_account_dual_type
        )


class GoEthereumVersionModuleTest(VersionModuleTest):
    pass


class GoEthereumNetModuleTest(NetModuleTest):
    pass


class CommonGoEthereumShhModuleTest(GoEthereumShhModuleTest):
    pass


class GoEthereumAdminModuleTest(GoEthereumAdminModuleTest):
    pass


class GoEthereumPersonalModuleTest(GoEthereumPersonalModuleTest):
    pass
