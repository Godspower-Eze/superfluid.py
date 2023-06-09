cfa_v1_forwarder = '''[
  {
    "inputs": [
      {
        "internalType": "contract ISuperfluid",
        "name": "host",
        "type": "address"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  { "inputs": [], "name": "CFA_FWD_INVALID_FLOW_RATE", "type": "error" },
  {
    "inputs": [
      {
        "internalType": "contract ISuperToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "sender", "type": "address" },
      { "internalType": "address", "name": "receiver", "type": "address" },
      { "internalType": "int96", "name": "flowrate", "type": "int96" },
      { "internalType": "bytes", "name": "userData", "type": "bytes" }
    ],
    "name": "createFlow",
    "outputs": [{ "internalType": "bool", "name": "", "type": "bool" }],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "sender", "type": "address" },
      { "internalType": "address", "name": "receiver", "type": "address" },
      { "internalType": "bytes", "name": "userData", "type": "bytes" }
    ],
    "name": "deleteFlow",
    "outputs": [{ "internalType": "bool", "name": "", "type": "bool" }],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "account", "type": "address" }
    ],
    "name": "getAccountFlowInfo",
    "outputs": [
      { "internalType": "uint256", "name": "lastUpdated", "type": "uint256" },
      { "internalType": "int96", "name": "flowrate", "type": "int96" },
      { "internalType": "uint256", "name": "deposit", "type": "uint256" },
      { "internalType": "uint256", "name": "owedDeposit", "type": "uint256" }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "account", "type": "address" }
    ],
    "name": "getAccountFlowrate",
    "outputs": [
      { "internalType": "int96", "name": "flowrate", "type": "int96" }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "int96", "name": "flowrate", "type": "int96" }
    ],
    "name": "getBufferAmountByFlowrate",
    "outputs": [
      { "internalType": "uint256", "name": "bufferAmount", "type": "uint256" }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "sender", "type": "address" },
      { "internalType": "address", "name": "receiver", "type": "address" }
    ],
    "name": "getFlowInfo",
    "outputs": [
      { "internalType": "uint256", "name": "lastUpdated", "type": "uint256" },
      { "internalType": "int96", "name": "flowrate", "type": "int96" },
      { "internalType": "uint256", "name": "deposit", "type": "uint256" },
      { "internalType": "uint256", "name": "owedDeposit", "type": "uint256" }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "sender", "type": "address" },
      { "internalType": "address", "name": "flowOperator", "type": "address" }
    ],
    "name": "getFlowOperatorPermissions",
    "outputs": [
      { "internalType": "uint8", "name": "permissions", "type": "uint8" },
      { "internalType": "int96", "name": "flowrateAllowance", "type": "int96" }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "sender", "type": "address" },
      { "internalType": "address", "name": "receiver", "type": "address" }
    ],
    "name": "getFlowrate",
    "outputs": [
      { "internalType": "int96", "name": "flowrate", "type": "int96" }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "flowOperator", "type": "address" }
    ],
    "name": "grantPermissions",
    "outputs": [{ "internalType": "bool", "name": "", "type": "bool" }],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "flowOperator", "type": "address" }
    ],
    "name": "revokePermissions",
    "outputs": [{ "internalType": "bool", "name": "", "type": "bool" }],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "receiver", "type": "address" },
      { "internalType": "int96", "name": "flowrate", "type": "int96" }
    ],
    "name": "setFlowrate",
    "outputs": [{ "internalType": "bool", "name": "", "type": "bool" }],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "sender", "type": "address" },
      { "internalType": "address", "name": "receiver", "type": "address" },
      { "internalType": "int96", "name": "flowrate", "type": "int96" }
    ],
    "name": "setFlowrateFrom",
    "outputs": [{ "internalType": "bool", "name": "", "type": "bool" }],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "sender", "type": "address" },
      { "internalType": "address", "name": "receiver", "type": "address" },
      { "internalType": "int96", "name": "flowrate", "type": "int96" },
      { "internalType": "bytes", "name": "userData", "type": "bytes" }
    ],
    "name": "updateFlow",
    "outputs": [{ "internalType": "bool", "name": "", "type": "bool" }],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "flowOperator", "type": "address" },
      { "internalType": "uint8", "name": "permissions", "type": "uint8" },
      { "internalType": "int96", "name": "flowrateAllowance", "type": "int96" }
    ],
    "name": "updateFlowOperatorPermissions",
    "outputs": [{ "internalType": "bool", "name": "", "type": "bool" }],
    "stateMutability": "nonpayable",
    "type": "function"
  }
]
'''

cfa_v1 = '''[
  {
    "inputs": [
      {
        "internalType": "contract ISuperfluid",
        "name": "host",
        "type": "address"
      },
      {
        "internalType": "contract IConstantFlowAgreementHook",
        "name": "_hookAddress",
        "type": "address"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "inputs": [
      { "internalType": "uint256", "name": "_code", "type": "uint256" }
    ],
    "name": "ALREADY_EXISTS",
    "type": "error"
  },
  {
    "inputs": [
      { "internalType": "uint256", "name": "_code", "type": "uint256" }
    ],
    "name": "APP_RULE",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "CFA_ACL_FLOW_RATE_ALLOWANCE_EXCEEDED",
    "type": "error"
  },
  { "inputs": [], "name": "CFA_ACL_NO_NEGATIVE_ALLOWANCE", "type": "error" },
  { "inputs": [], "name": "CFA_ACL_NO_SENDER_CREATE", "type": "error" },
  { "inputs": [], "name": "CFA_ACL_NO_SENDER_FLOW_OPERATOR", "type": "error" },
  { "inputs": [], "name": "CFA_ACL_NO_SENDER_UPDATE", "type": "error" },
  {
    "inputs": [],
    "name": "CFA_ACL_OPERATOR_NO_CREATE_PERMISSIONS",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "CFA_ACL_OPERATOR_NO_DELETE_PERMISSIONS",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "CFA_ACL_OPERATOR_NO_UPDATE_PERMISSIONS",
    "type": "error"
  },
  { "inputs": [], "name": "CFA_ACL_UNCLEAN_PERMISSIONS", "type": "error" },
  { "inputs": [], "name": "CFA_DEPOSIT_TOO_BIG", "type": "error" },
  { "inputs": [], "name": "CFA_FLOW_RATE_TOO_BIG", "type": "error" },
  { "inputs": [], "name": "CFA_INVALID_FLOW_RATE", "type": "error" },
  { "inputs": [], "name": "CFA_NON_CRITICAL_SENDER", "type": "error" },
  { "inputs": [], "name": "CFA_NO_SELF_FLOW", "type": "error" },
  {
    "inputs": [
      { "internalType": "uint256", "name": "_code", "type": "uint256" }
    ],
    "name": "DOES_NOT_EXIST",
    "type": "error"
  },
  {
    "inputs": [
      { "internalType": "uint256", "name": "_code", "type": "uint256" }
    ],
    "name": "INSUFFICIENT_BALANCE",
    "type": "error"
  },
  {
    "inputs": [
      { "internalType": "uint256", "name": "_code", "type": "uint256" }
    ],
    "name": "ONLY_HOST",
    "type": "error"
  },
  {
    "inputs": [
      { "internalType": "uint256", "name": "_code", "type": "uint256" }
    ],
    "name": "OUT_OF_GAS",
    "type": "error"
  },
  {
    "inputs": [
      { "internalType": "uint256", "name": "_code", "type": "uint256" }
    ],
    "name": "ZERO_ADDRESS",
    "type": "error"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": false,
        "internalType": "bytes32",
        "name": "uuid",
        "type": "bytes32"
      },
      {
        "indexed": false,
        "internalType": "address",
        "name": "codeAddress",
        "type": "address"
      }
    ],
    "name": "CodeUpdated",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "contract ISuperfluidToken",
        "name": "token",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "sender",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "flowOperator",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "uint8",
        "name": "permissions",
        "type": "uint8"
      },
      {
        "indexed": false,
        "internalType": "int96",
        "name": "flowRateAllowance",
        "type": "int96"
      }
    ],
    "name": "FlowOperatorUpdated",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "contract ISuperfluidToken",
        "name": "token",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "sender",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "receiver",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "int96",
        "name": "flowRate",
        "type": "int96"
      },
      {
        "indexed": false,
        "internalType": "int256",
        "name": "totalSenderFlowRate",
        "type": "int256"
      },
      {
        "indexed": false,
        "internalType": "int256",
        "name": "totalReceiverFlowRate",
        "type": "int256"
      },
      {
        "indexed": false,
        "internalType": "bytes",
        "name": "userData",
        "type": "bytes"
      }
    ],
    "name": "FlowUpdated",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "flowOperator",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "deposit",
        "type": "uint256"
      }
    ],
    "name": "FlowUpdatedExtension",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": false,
        "internalType": "uint8",
        "name": "version",
        "type": "uint8"
      }
    ],
    "name": "Initialized",
    "type": "event"
  },
  {
    "inputs": [],
    "name": "CFA_HOOK_GAS_LIMIT",
    "outputs": [{ "internalType": "uint64", "name": "", "type": "uint64" }],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "DEFAULT_MINIMUM_DEPOSIT",
    "outputs": [{ "internalType": "uint256", "name": "", "type": "uint256" }],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "MAXIMUM_DEPOSIT",
    "outputs": [{ "internalType": "uint256", "name": "", "type": "uint256" }],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "MAXIMUM_FLOW_RATE",
    "outputs": [{ "internalType": "uint256", "name": "", "type": "uint256" }],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "agreementType",
    "outputs": [{ "internalType": "bytes32", "name": "", "type": "bytes32" }],
    "stateMutability": "pure",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperfluidToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "flowOperator", "type": "address" },
      { "internalType": "bytes", "name": "ctx", "type": "bytes" }
    ],
    "name": "authorizeFlowOperatorWithFullControl",
    "outputs": [{ "internalType": "bytes", "name": "newCtx", "type": "bytes" }],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "castrate",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "constantFlowAgreementHook",
    "outputs": [
      {
        "internalType": "contract IConstantFlowAgreementHook",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperfluidToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "receiver", "type": "address" },
      { "internalType": "int96", "name": "flowRate", "type": "int96" },
      { "internalType": "bytes", "name": "ctx", "type": "bytes" }
    ],
    "name": "createFlow",
    "outputs": [{ "internalType": "bytes", "name": "newCtx", "type": "bytes" }],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperfluidToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "sender", "type": "address" },
      { "internalType": "address", "name": "receiver", "type": "address" },
      { "internalType": "int96", "name": "flowRate", "type": "int96" },
      { "internalType": "bytes", "name": "ctx", "type": "bytes" }
    ],
    "name": "createFlowByOperator",
    "outputs": [{ "internalType": "bytes", "name": "newCtx", "type": "bytes" }],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperfluidToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "sender", "type": "address" },
      { "internalType": "address", "name": "receiver", "type": "address" },
      { "internalType": "bytes", "name": "ctx", "type": "bytes" }
    ],
    "name": "deleteFlow",
    "outputs": [{ "internalType": "bytes", "name": "newCtx", "type": "bytes" }],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperfluidToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "sender", "type": "address" },
      { "internalType": "address", "name": "receiver", "type": "address" },
      { "internalType": "bytes", "name": "ctx", "type": "bytes" }
    ],
    "name": "deleteFlowByOperator",
    "outputs": [{ "internalType": "bytes", "name": "newCtx", "type": "bytes" }],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperfluidToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "account", "type": "address" }
    ],
    "name": "getAccountFlowInfo",
    "outputs": [
      { "internalType": "uint256", "name": "timestamp", "type": "uint256" },
      { "internalType": "int96", "name": "flowRate", "type": "int96" },
      { "internalType": "uint256", "name": "deposit", "type": "uint256" },
      { "internalType": "uint256", "name": "owedDeposit", "type": "uint256" }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "getCodeAddress",
    "outputs": [
      { "internalType": "address", "name": "codeAddress", "type": "address" }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperfluidToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "int96", "name": "flowRate", "type": "int96" }
    ],
    "name": "getDepositRequiredForFlowRate",
    "outputs": [
      { "internalType": "uint256", "name": "deposit", "type": "uint256" }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperfluidToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "sender", "type": "address" },
      { "internalType": "address", "name": "receiver", "type": "address" }
    ],
    "name": "getFlow",
    "outputs": [
      { "internalType": "uint256", "name": "timestamp", "type": "uint256" },
      { "internalType": "int96", "name": "flowRate", "type": "int96" },
      { "internalType": "uint256", "name": "deposit", "type": "uint256" },
      { "internalType": "uint256", "name": "owedDeposit", "type": "uint256" }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperfluidToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "bytes32", "name": "flowId", "type": "bytes32" }
    ],
    "name": "getFlowByID",
    "outputs": [
      { "internalType": "uint256", "name": "timestamp", "type": "uint256" },
      { "internalType": "int96", "name": "flowRate", "type": "int96" },
      { "internalType": "uint256", "name": "deposit", "type": "uint256" },
      { "internalType": "uint256", "name": "owedDeposit", "type": "uint256" }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperfluidToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "sender", "type": "address" },
      { "internalType": "address", "name": "flowOperator", "type": "address" }
    ],
    "name": "getFlowOperatorData",
    "outputs": [
      {
        "internalType": "bytes32",
        "name": "flowOperatorId",
        "type": "bytes32"
      },
      { "internalType": "uint8", "name": "permissions", "type": "uint8" },
      { "internalType": "int96", "name": "flowRateAllowance", "type": "int96" }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperfluidToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "bytes32", "name": "flowOperatorId", "type": "bytes32" }
    ],
    "name": "getFlowOperatorDataByID",
    "outputs": [
      { "internalType": "uint8", "name": "permissions", "type": "uint8" },
      { "internalType": "int96", "name": "flowRateAllowance", "type": "int96" }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperfluidToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "uint256", "name": "deposit", "type": "uint256" }
    ],
    "name": "getMaximumFlowRateFromDeposit",
    "outputs": [
      { "internalType": "int96", "name": "flowRate", "type": "int96" }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperfluidToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "account", "type": "address" }
    ],
    "name": "getNetFlow",
    "outputs": [
      { "internalType": "int96", "name": "flowRate", "type": "int96" }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperfluidToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "account", "type": "address" },
      { "internalType": "uint256", "name": "timestamp", "type": "uint256" }
    ],
    "name": "isPatricianPeriod",
    "outputs": [{ "internalType": "bool", "name": "", "type": "bool" }],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperfluidToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "account", "type": "address" }
    ],
    "name": "isPatricianPeriodNow",
    "outputs": [
      {
        "internalType": "bool",
        "name": "isCurrentlyPatricianPeriod",
        "type": "bool"
      },
      { "internalType": "uint256", "name": "timestamp", "type": "uint256" }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "proxiableUUID",
    "outputs": [{ "internalType": "bytes32", "name": "", "type": "bytes32" }],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperfluidToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "account", "type": "address" },
      { "internalType": "uint256", "name": "time", "type": "uint256" }
    ],
    "name": "realtimeBalanceOf",
    "outputs": [
      { "internalType": "int256", "name": "dynamicBalance", "type": "int256" },
      { "internalType": "uint256", "name": "deposit", "type": "uint256" },
      { "internalType": "uint256", "name": "owedDeposit", "type": "uint256" }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperfluidToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "flowOperator", "type": "address" },
      { "internalType": "bytes", "name": "ctx", "type": "bytes" }
    ],
    "name": "revokeFlowOperatorWithFullControl",
    "outputs": [{ "internalType": "bytes", "name": "newCtx", "type": "bytes" }],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      { "internalType": "address", "name": "newAddress", "type": "address" }
    ],
    "name": "updateCode",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperfluidToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "receiver", "type": "address" },
      { "internalType": "int96", "name": "flowRate", "type": "int96" },
      { "internalType": "bytes", "name": "ctx", "type": "bytes" }
    ],
    "name": "updateFlow",
    "outputs": [{ "internalType": "bytes", "name": "newCtx", "type": "bytes" }],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperfluidToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "sender", "type": "address" },
      { "internalType": "address", "name": "receiver", "type": "address" },
      { "internalType": "int96", "name": "flowRate", "type": "int96" },
      { "internalType": "bytes", "name": "ctx", "type": "bytes" }
    ],
    "name": "updateFlowByOperator",
    "outputs": [{ "internalType": "bytes", "name": "newCtx", "type": "bytes" }],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperfluidToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "flowOperator", "type": "address" },
      { "internalType": "uint8", "name": "permissions", "type": "uint8" },
      { "internalType": "int96", "name": "flowRateAllowance", "type": "int96" },
      { "internalType": "bytes", "name": "ctx", "type": "bytes" }
    ],
    "name": "updateFlowOperatorPermissions",
    "outputs": [{ "internalType": "bytes", "name": "newCtx", "type": "bytes" }],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperfluidToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "flowOperator", "type": "address" },
      { "internalType": "int96", "name": "addedFlowRateAllowance", "type": "int96" },
      { "internalType": "bytes", "name": "ctx", "type": "bytes" }
    ],
    "name": "increaseFlowRateAllowance",
    "outputs": [{ "internalType": "bytes", "name": "newCtx", "type": "bytes" }],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperfluidToken",
        "name": "token",
        "type": "address"
      },
      { "internalType": "address", "name": "flowOperator", "type": "address" },
      { "internalType": "int96", "name": "subtractedFlowRateAllowance", "type": "int96" },
      { "internalType": "bytes", "name": "ctx", "type": "bytes" }
    ],
    "name": "decreaseFlowRateAllowance",
    "outputs": [{ "internalType": "bytes", "name": "newCtx", "type": "bytes" }],
    "stateMutability": "nonpayable",
    "type": "function"
  }
]
'''

host = '''[
  {
    "inputs": [
      { "internalType": "bool", "name": "nonUpgradable", "type": "bool" },
      {
        "internalType": "bool",
        "name": "appWhiteListingEnabled",
        "type": "bool"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "inputs": [
      { "internalType": "uint256", "name": "_code", "type": "uint256" }
    ],
    "name": "ALREADY_EXISTS",
    "type": "error"
  },
  {
    "inputs": [
      { "internalType": "uint256", "name": "_code", "type": "uint256" }
    ],
    "name": "APP_RULE",
    "type": "error"
  },
  {
    "inputs": [
      { "internalType": "uint256", "name": "_code", "type": "uint256" }
    ],
    "name": "DOES_NOT_EXIST",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "HOST_AGREEMENT_CALLBACK_IS_NOT_ACTION",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "HOST_CALL_AGREEMENT_WITH_CTX_FROM_WRONG_ADDRESS",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "HOST_CALL_APP_ACTION_WITH_CTX_FROM_WRONG_ADDRESS",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "HOST_CANNOT_DOWNGRADE_TO_NON_UPGRADEABLE",
    "type": "error"
  },
  { "inputs": [], "name": "HOST_INVALID_CONFIG_WORD", "type": "error" },
  {
    "inputs": [],
    "name": "HOST_INVALID_OR_EXPIRED_SUPER_APP_REGISTRATION_KEY",
    "type": "error"
  },
  { "inputs": [], "name": "HOST_MAX_256_AGREEMENTS", "type": "error" },
  { "inputs": [], "name": "HOST_NON_UPGRADEABLE", "type": "error" },
  {
    "inputs": [],
    "name": "HOST_NON_ZERO_LENGTH_PLACEHOLDER_CTX",
    "type": "error"
  },
  { "inputs": [], "name": "HOST_NOT_A_SUPER_APP", "type": "error" },
  {
    "inputs": [],
    "name": "HOST_NO_APP_REGISTRATION_PERMISSIONS",
    "type": "error"
  },
  { "inputs": [], "name": "HOST_ONLY_GOVERNANCE", "type": "error" },
  { "inputs": [], "name": "HOST_RECEIVER_IS_NOT_SUPER_APP", "type": "error" },
  { "inputs": [], "name": "HOST_SENDER_IS_NOT_SUPER_APP", "type": "error" },
  {
    "inputs": [],
    "name": "HOST_SOURCE_APP_NEEDS_HIGHER_APP_LEVEL",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "HOST_SUPER_APP_ALREADY_REGISTERED",
    "type": "error"
  },
  { "inputs": [], "name": "HOST_SUPER_APP_IS_JAILED", "type": "error" },
  {
    "inputs": [],
    "name": "HOST_UNAUTHORIZED_SUPER_APP_FACTORY",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "HOST_UNKNOWN_BATCH_CALL_OPERATION_TYPE",
    "type": "error"
  },
  {
    "inputs": [
      { "internalType": "uint256", "name": "_code", "type": "uint256" }
    ],
    "name": "MUST_BE_CONTRACT",
    "type": "error"
  },
  {
    "inputs": [
      { "internalType": "uint256", "name": "_code", "type": "uint256" }
    ],
    "name": "ONLY_LISTED_AGREEMENT",
    "type": "error"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": false,
        "internalType": "bytes32",
        "name": "agreementType",
        "type": "bytes32"
      },
      {
        "indexed": false,
        "internalType": "address",
        "name": "code",
        "type": "address"
      }
    ],
    "name": "AgreementClassRegistered",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": false,
        "internalType": "bytes32",
        "name": "agreementType",
        "type": "bytes32"
      },
      {
        "indexed": false,
        "internalType": "address",
        "name": "code",
        "type": "address"
      }
    ],
    "name": "AgreementClassUpdated",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "contract ISuperApp",
        "name": "app",
        "type": "address"
      }
    ],
    "name": "AppRegistered",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": false,
        "internalType": "bytes32",
        "name": "uuid",
        "type": "bytes32"
      },
      {
        "indexed": false,
        "internalType": "address",
        "name": "codeAddress",
        "type": "address"
      }
    ],
    "name": "CodeUpdated",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": false,
        "internalType": "contract ISuperfluidGovernance",
        "name": "oldGov",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "contract ISuperfluidGovernance",
        "name": "newGov",
        "type": "address"
      }
    ],
    "name": "GovernanceReplaced",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": false,
        "internalType": "uint8",
        "name": "version",
        "type": "uint8"
      }
    ],
    "name": "Initialized",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "contract ISuperApp",
        "name": "app",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "reason",
        "type": "uint256"
      }
    ],
    "name": "Jail",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": false,
        "internalType": "contract ISuperTokenFactory",
        "name": "newFactory",
        "type": "address"
      }
    ],
    "name": "SuperTokenFactoryUpdated",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "contract ISuperToken",
        "name": "token",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "address",
        "name": "code",
        "type": "address"
      }
    ],
    "name": "SuperTokenLogicUpdated",
    "type": "event"
  },
  {
    "inputs": [],
    "name": "APP_WHITE_LISTING_ENABLED",
    "outputs": [{ "internalType": "bool", "name": "", "type": "bool" }],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "CALLBACK_GAS_LIMIT",
    "outputs": [{ "internalType": "uint64", "name": "", "type": "uint64" }],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "NON_UPGRADABLE_DEPLOYMENT",
    "outputs": [{ "internalType": "bool", "name": "", "type": "bool" }],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      { "internalType": "uint256", "name": "bitmap", "type": "uint256" },
      { "internalType": "bytes32", "name": "agreementType", "type": "bytes32" }
    ],
    "name": "addToAgreementClassesBitmap",
    "outputs": [
      { "internalType": "uint256", "name": "newBitmap", "type": "uint256" }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperApp",
        "name": "targetApp",
        "type": "address"
      }
    ],
    "name": "allowCompositeApp",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      { "internalType": "bytes", "name": "ctx", "type": "bytes" },
      {
        "internalType": "int256",
        "name": "appCreditUsedDelta",
        "type": "int256"
      }
    ],
    "name": "appCallbackPop",
    "outputs": [{ "internalType": "bytes", "name": "newCtx", "type": "bytes" }],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      { "internalType": "bytes", "name": "ctx", "type": "bytes" },
      {
        "internalType": "contract ISuperApp",
        "name": "app",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "appCreditGranted",
        "type": "uint256"
      },
      { "internalType": "int256", "name": "appCreditUsed", "type": "int256" },
      {
        "internalType": "contract ISuperfluidToken",
        "name": "appCreditToken",
        "type": "address"
      }
    ],
    "name": "appCallbackPush",
    "outputs": [{ "internalType": "bytes", "name": "appCtx", "type": "bytes" }],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "components": [
          {
            "internalType": "uint32",
            "name": "operationType",
            "type": "uint32"
          },
          { "internalType": "address", "name": "target", "type": "address" },
          { "internalType": "bytes", "name": "data", "type": "bytes" }
        ],
        "internalType": "struct ISuperfluid.Operation[]",
        "name": "operations",
        "type": "tuple[]"
      }
    ],
    "name": "batchCall",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperAgreement",
        "name": "agreementClass",
        "type": "address"
      },
      { "internalType": "bytes", "name": "callData", "type": "bytes" },
      { "internalType": "bytes", "name": "userData", "type": "bytes" }
    ],
    "name": "callAgreement",
    "outputs": [
      { "internalType": "bytes", "name": "returnedData", "type": "bytes" }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperAgreement",
        "name": "agreementClass",
        "type": "address"
      },
      { "internalType": "bytes", "name": "callData", "type": "bytes" },
      { "internalType": "bytes", "name": "userData", "type": "bytes" },
      { "internalType": "bytes", "name": "ctx", "type": "bytes" }
    ],
    "name": "callAgreementWithContext",
    "outputs": [
      { "internalType": "bytes", "name": "newCtx", "type": "bytes" },
      { "internalType": "bytes", "name": "returnedData", "type": "bytes" }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperApp",
        "name": "app",
        "type": "address"
      },
      { "internalType": "bytes", "name": "callData", "type": "bytes" }
    ],
    "name": "callAppAction",
    "outputs": [
      { "internalType": "bytes", "name": "returnedData", "type": "bytes" }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperApp",
        "name": "app",
        "type": "address"
      },
      { "internalType": "bytes", "name": "callData", "type": "bytes" },
      { "internalType": "bytes", "name": "ctx", "type": "bytes" }
    ],
    "name": "callAppActionWithContext",
    "outputs": [{ "internalType": "bytes", "name": "newCtx", "type": "bytes" }],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperApp",
        "name": "app",
        "type": "address"
      },
      { "internalType": "bytes", "name": "callData", "type": "bytes" },
      { "internalType": "bool", "name": "isTermination", "type": "bool" },
      { "internalType": "bytes", "name": "ctx", "type": "bytes" }
    ],
    "name": "callAppAfterCallback",
    "outputs": [{ "internalType": "bytes", "name": "newCtx", "type": "bytes" }],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperApp",
        "name": "app",
        "type": "address"
      },
      { "internalType": "bytes", "name": "callData", "type": "bytes" },
      { "internalType": "bool", "name": "isTermination", "type": "bool" },
      { "internalType": "bytes", "name": "ctx", "type": "bytes" }
    ],
    "name": "callAppBeforeCallback",
    "outputs": [{ "internalType": "bytes", "name": "cbdata", "type": "bytes" }],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "castrate",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      { "internalType": "bytes", "name": "ctx", "type": "bytes" },
      {
        "internalType": "int256",
        "name": "appCreditUsedMore",
        "type": "int256"
      }
    ],
    "name": "ctxUseCredit",
    "outputs": [{ "internalType": "bytes", "name": "newCtx", "type": "bytes" }],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [{ "internalType": "bytes", "name": "ctx", "type": "bytes" }],
    "name": "decodeCtx",
    "outputs": [
      {
        "components": [
          {
            "internalType": "uint8",
            "name": "appCallbackLevel",
            "type": "uint8"
          },
          { "internalType": "uint8", "name": "callType", "type": "uint8" },
          { "internalType": "uint256", "name": "timestamp", "type": "uint256" },
          { "internalType": "address", "name": "msgSender", "type": "address" },
          {
            "internalType": "bytes4",
            "name": "agreementSelector",
            "type": "bytes4"
          },
          { "internalType": "bytes", "name": "userData", "type": "bytes" },
          {
            "internalType": "uint256",
            "name": "appCreditGranted",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "appCreditWantedDeprecated",
            "type": "uint256"
          },
          {
            "internalType": "int256",
            "name": "appCreditUsed",
            "type": "int256"
          },
          {
            "internalType": "address",
            "name": "appAddress",
            "type": "address"
          },
          {
            "internalType": "contract ISuperfluidToken",
            "name": "appCreditToken",
            "type": "address"
          }
        ],
        "internalType": "struct ISuperfluid.Context",
        "name": "context",
        "type": "tuple"
      }
    ],
    "stateMutability": "pure",
    "type": "function"
  },
  {
    "inputs": [
      {
        "components": [
          {
            "internalType": "uint32",
            "name": "operationType",
            "type": "uint32"
          },
          { "internalType": "address", "name": "target", "type": "address" },
          { "internalType": "bytes", "name": "data", "type": "bytes" }
        ],
        "internalType": "struct ISuperfluid.Operation[]",
        "name": "operations",
        "type": "tuple[]"
      }
    ],
    "name": "forwardBatchCall",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      { "internalType": "bytes32", "name": "agreementType", "type": "bytes32" }
    ],
    "name": "getAgreementClass",
    "outputs": [
      {
        "internalType": "contract ISuperAgreement",
        "name": "agreementClass",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperApp",
        "name": "appAddr",
        "type": "address"
      }
    ],
    "name": "getAppCallbackLevel",
    "outputs": [{ "internalType": "uint8", "name": "", "type": "uint8" }],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      { "internalType": "contract ISuperApp", "name": "app", "type": "address" }
    ],
    "name": "getAppManifest",
    "outputs": [
      { "internalType": "bool", "name": "isSuperApp", "type": "bool" },
      { "internalType": "bool", "name": "isJailed", "type": "bool" },
      { "internalType": "uint256", "name": "noopMask", "type": "uint256" }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "getCodeAddress",
    "outputs": [
      { "internalType": "address", "name": "codeAddress", "type": "address" }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "getGovernance",
    "outputs": [
      {
        "internalType": "contract ISuperfluidGovernance",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "getNow",
    "outputs": [{ "internalType": "uint256", "name": "", "type": "uint256" }],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "getSuperTokenFactory",
    "outputs": [
      {
        "internalType": "contract ISuperTokenFactory",
        "name": "factory",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "getSuperTokenFactoryLogic",
    "outputs": [
      { "internalType": "address", "name": "logic", "type": "address" }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperfluidGovernance",
        "name": "gov",
        "type": "address"
      }
    ],
    "name": "initialize",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperAgreement",
        "name": "agreementClass",
        "type": "address"
      }
    ],
    "name": "isAgreementClassListed",
    "outputs": [{ "internalType": "bool", "name": "yes", "type": "bool" }],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      { "internalType": "bytes32", "name": "agreementType", "type": "bytes32" }
    ],
    "name": "isAgreementTypeListed",
    "outputs": [{ "internalType": "bool", "name": "yes", "type": "bool" }],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      { "internalType": "contract ISuperApp", "name": "app", "type": "address" }
    ],
    "name": "isApp",
    "outputs": [{ "internalType": "bool", "name": "", "type": "bool" }],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      { "internalType": "contract ISuperApp", "name": "app", "type": "address" }
    ],
    "name": "isAppJailed",
    "outputs": [{ "internalType": "bool", "name": "", "type": "bool" }],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperApp",
        "name": "app",
        "type": "address"
      },
      {
        "internalType": "contract ISuperApp",
        "name": "targetApp",
        "type": "address"
      }
    ],
    "name": "isCompositeAppAllowed",
    "outputs": [{ "internalType": "bool", "name": "", "type": "bool" }],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [{ "internalType": "bytes", "name": "ctx", "type": "bytes" }],
    "name": "isCtxValid",
    "outputs": [{ "internalType": "bool", "name": "", "type": "bool" }],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      { "internalType": "address", "name": "forwarder", "type": "address" }
    ],
    "name": "isTrustedForwarder",
    "outputs": [{ "internalType": "bool", "name": "", "type": "bool" }],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      { "internalType": "bytes", "name": "ctx", "type": "bytes" },
      {
        "internalType": "contract ISuperApp",
        "name": "app",
        "type": "address"
      },
      { "internalType": "uint256", "name": "reason", "type": "uint256" }
    ],
    "name": "jailApp",
    "outputs": [{ "internalType": "bytes", "name": "newCtx", "type": "bytes" }],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      { "internalType": "uint256", "name": "bitmap", "type": "uint256" }
    ],
    "name": "mapAgreementClasses",
    "outputs": [
      {
        "internalType": "contract ISuperAgreement[]",
        "name": "agreementClasses",
        "type": "address[]"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "proxiableUUID",
    "outputs": [{ "internalType": "bytes32", "name": "", "type": "bytes32" }],
    "stateMutability": "pure",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperAgreement",
        "name": "agreementClassLogic",
        "type": "address"
      }
    ],
    "name": "registerAgreementClass",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      { "internalType": "uint256", "name": "configWord", "type": "uint256" }
    ],
    "name": "registerApp",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperApp",
        "name": "app",
        "type": "address"
      },
      { "internalType": "uint256", "name": "configWord", "type": "uint256" }
    ],
    "name": "registerAppByFactory",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      { "internalType": "uint256", "name": "configWord", "type": "uint256" },
      { "internalType": "string", "name": "registrationKey", "type": "string" }
    ],
    "name": "registerAppWithKey",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      { "internalType": "uint256", "name": "bitmap", "type": "uint256" },
      { "internalType": "bytes32", "name": "agreementType", "type": "bytes32" }
    ],
    "name": "removeFromAgreementClassesBitmap",
    "outputs": [
      { "internalType": "uint256", "name": "newBitmap", "type": "uint256" }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperfluidGovernance",
        "name": "newGov",
        "type": "address"
      }
    ],
    "name": "replaceGovernance",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperAgreement",
        "name": "agreementClassLogic",
        "type": "address"
      }
    ],
    "name": "updateAgreementClass",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      { "internalType": "address", "name": "newAddress", "type": "address" }
    ],
    "name": "updateCode",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperTokenFactory",
        "name": "newFactory",
        "type": "address"
      }
    ],
    "name": "updateSuperTokenFactory",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "contract ISuperToken",
        "name": "token",
        "type": "address"
      }
    ],
    "name": "updateSuperTokenLogic",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "versionRecipient",
    "outputs": [{ "internalType": "string", "name": "", "type": "string" }],
    "stateMutability": "pure",
    "type": "function"
  }
]
'''
