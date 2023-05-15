from typing import Dict, Union

from web3 import Web3

from host import Host
from constants import CFA_V1_ABI, CFA_V1_FORWARDER_ABI, RPC_FOR_MUMBAI, CFA_V1_ADDRESS, CFA_V1_FORWARDER_ADDRESS, HOST_ADDRESS
from __types__ import GetFlowParams, GetAccountFlowInfoParams, GetFlowOperatorDataParams, GetFlowOperatorDataParamsByID, CreateFlowParams
from errors import SFError
from operation import Operation
from utils import to_bytes32


class CFA_V1:

    web3 = None
    host = None
    contract = None
    forwarder = None

    def __init__(self, rpc: str, host_address: str, cfa_v1_address: str, cfa_v1_forwarder: str) -> None:
        web3 = Web3(Web3.HTTPProvider(rpc))
        web3.strict_bytes_type_checking = False
        self.host = Host(rpc, host_address)
        self.contract = web3.eth.contract(
            address=cfa_v1_address, abi=CFA_V1_ABI)
        self.forwarder = web3.eth.contract(
            address=cfa_v1_forwarder, abi=CFA_V1_FORWARDER_ABI)

    def get_flow(self, params: GetFlowParams) -> Dict[str, int]:
        """
            Get the details of a flow.
            @param params holds the super token, sender, and receiver
            @returns  Dict[str, int] Web3 Flow info object:

            flow_data = {
                "timestamp": int,
                "flowRate": int,
                "deposit": int,
                "owedDeposit": int
            }
        """
        try:
            transaction_response = self.contract.functions.getFlow(
                params.super_token, params.sender, params.receiver).call()
            flow_data = {
                "timestamp": transaction_response[0],
                "flowRate": transaction_response[1],
                "deposit": transaction_response[2],
                "owedDeposit": transaction_response[3]
            }
            return flow_data
        except Exception as e:
            raise SFError(e)

    def get_account_flow_info(self, params: GetAccountFlowInfoParams) -> Dict[str, int]:
        """
            Get the details of a account flow in a super token.
            @param params holds the super token and account
            @returns  Dict[str, int] Web3 Account Flow info object:

            info = {
                "timestamp": int,
                "flowRate": int,
                "deposit": int,
                "owedDeposit": int
            }
        """
        try:
            transaction_response = self.contract.functions.getAccountFlowInfo(
                params.super_token, params.account).call()
            info = {
                "timestamp": transaction_response[0],
                "flowRate": transaction_response[1],
                "deposit": transaction_response[2],
                "owedDeposit": transaction_response[3]
            }
            return info
        except Exception as e:
            raise SFError(e)

    def get_net_flow(self, params: GetAccountFlowInfoParams) -> int:
        """
            Get the details of the net flow of an account in a super token.
            @param params holds the super token and account
            @returns int net flow rate of the account
        """
        try:
            transaction_response = self.contract.functions.getNetFlow(
                params.super_token, params.account).call()
            net_flow_rate = transaction_response
            return net_flow_rate
        except Exception as e:
            raise SFError(e)

    def get_flow_operator_data(self, params: GetFlowOperatorDataParams) -> Dict[str, int]:
        """
            Get the details of a flow operator to a sender
            @param params holds the super token, sender and flow operator
            @returns Dict[str, int] Web3 Flow Operator info object:

            flow_operator_data = {
                "flowOperatorId": str,
                "permissions": int,
                "flowRateAllowance": int
            }
        """
        try:
            transaction_response = self.contract.functions.getFlowOperatorData(
                params.super_token, params.sender, params.flow_operator).call()
            flow_operator_data = {
                # TODO: Review conversions
                "flowOperatorId": Web3.to_hex(transaction_response[0]),
                "permissions": transaction_response[1],
                "flowRateAllowance": transaction_response[2]
            }
            return flow_operator_data
        except Exception as e:
            raise SFError(e)

    def get_flow_operator_data_by_id(self, params: GetFlowOperatorDataParamsByID) -> Dict[str, int]:
        """
            Get the details of a flow operator to a sender by id
            @param params holds the super token and the flow operator id
            @returns Dict[str, int] Web3 Flow Operator info object:

            flow_operator_data = {
                "flowOperatorId": str,
                "permissions": int,
                "flowRateAllowance": int
            }
        """
        try:
            transaction_response = self.contract.functions.getFlowOperatorDataByID(
                params.super_token, params.flow_operator_id).call()
            flow_operator_data = {
                # TODO: Review conversions
                "flowOperatorId": params.flow_operator_id,
                "permissions": transaction_response[0],
                "flowRateAllowance": transaction_response[1]
            }
            return flow_operator_data
        except Exception as e:
            raise SFError(e)

    def create_flow(self, params: CreateFlowParams) -> Operation:
        calldata = self.contract.encodeABI(fn_name='createFlow', args=[
                                           params.super_token, params.receiver, params.flow_rate, "0x"])
        call_agreement_operation = self.host.call_agreement(
            self.contract.address, calldata, "0x")


# MANUAL TESTING
# cfaV1Instance = CFA_V1(RPC_FOR_MUMBAI, HOST_ADDRESS, CFA_V1_ADDRESS,
#                        CFA_V1_FORWARDER_ADDRESS)
# super_token = "0x5D8B4C2554aeB7e86F387B4d6c00Ac33499Ed01f"
# sender = "0xE895C0Cfb0f3CcE6844E9082989AC2Aa2ba8B253"
# receiver = "0x1d19ef8FC94D8aF1EC921Fd0B4978831D147EBf8"

# create_flow_params = CreateFlowParams(True, receiver, super_token, 10)
# response = cfaV1Instance.create_flow(create_flow_params)
