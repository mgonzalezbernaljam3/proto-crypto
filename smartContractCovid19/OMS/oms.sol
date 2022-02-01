//SPDX-license-dientifier GLP-3.0
pragma solidity >= 0.7.0 < 0.9.0; 
pragma external ABIEncoderV2;

contract OMS_COVID {

    //Address of the OMS -> Owner 
    address public OMS;

    //Constructr 
    constructor () public{
        OMS = msg.sender;
    }

    //What centers of helty have the certificate  to create PCR
    //Mapping for to relate health centers (address) to the validity of the health system
    mapping (address => bool) Validate_HealthCenter;
    //this help to us to relate the address with a bool(true or false) (have permission or haven't)

    //Mapping to relate health centers (address) to the Smart Contract
    mapping (address => address)public CenterHealth_Contract;


    //Array of address to have all the contracts Health centers validated
    address[] public address_contracts_health; 

    //Array to store the addresses that request access
    address[] access_requests;

    //Events
    event NewRequestsAccess(address);
    event NewHealthCenter(address);
    event NewContract(address, address);
    
    //We need a modifier that only allows the execution of functions by the OMS
    modifier OnlyOMS(address _address) {
        require (_address == OMS, "You do not have permission.");
        _;
    }

    // Function to request access to the Health Center
    function RequestsAccess() public {
        //save the address in the access_requests
        access_requests.push(msg.sender);
        //Emit event
        emit NewRequestsAccess(msg.sender);
    }


    //Function to validate new health centers that can be self-managed ==> Only OMS
    function HealthCenter (address _healthCenter) public OnlyOMS(msg.sender){
        // Assignment of the validity status to the health center
        Validate_HealthCenter[_healthCenter] = true;
        //Emit event
        emit NewHealthCenter(_healthCenter);
    }


    //Function to create a smart contract of the Health centers
    function FactoryHealthCenter () public {
        //Filtered so that only validated health centers are capable of executing this function 
        require (Validate_HealthCenter[msg.sender] == true, "You do not have permission.");

        //Generate a smart Contract --> Generate address 
        address contract_HealthCenter = address (new ContractHealthCenter(msg.sender));

        //save the address of the new contract in to array
        address_contracts_health.push(contract_HealthCenter);

        //Related the HealthCenter with the contract 
        CenterHealth_Contract[msg.sender] = contract_HealthCenter;

        //Emit event
        emit NewContract (contract_HealthCenter , msg.sender);

    }

    //Function to displays the addresses that have requested this access
    function DisplayRequests() public view OnlyOMS(msg.sender) returns(address[] memory) {
        return access_requests;
    }

}

// self-manageable contract by the health center
contract ContractHealthCenter {

        //initials address
        address public AddressContract;
        address public AddressHealthCenter;

        constructor (address _address) public {
            AddressHealthCenter =  _address;
            AddressContract = address(this);
        }

        //mapping to relate the hash of person with the reults (diagnosis , Code IPFS)
        mapping(bytes32 => Results) resultCOVID;

        //Structure of Results
        struct Results{
            bool diagnosis;
            string codeIPFS;
        }

        //Events
        event NewResult(string , bool);

        //Filter
        modifier OnlyHalthCenter(address _address) {
            require (_address == AddressHealthCenter, "You do not have permission.");
            _;
        }

        //Function to issue a result of a covid test
        function  ResultsTestCovid(string memory _idPerson, bool _resultCOVID, string memory _codeIPFS) public OnlyHalthCenter(msg.sender){
            //hash of the IDidentification of person
            bytes32 hash_idPerson = Keccak256 (abi, encodePacked(_idPerson));
            
            //Relate between the hash of person and the result f the test COVID
           resultCOVID [hash_idPerson] = Results(_resultCOVID, _codeIPFS );

            //Emit event
            emit NewResult (_resultCOVID , _codeIPFS); 

        }
 




}