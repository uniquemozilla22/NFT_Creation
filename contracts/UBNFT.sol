// SPDX-License-Identifier: MIT
pragma solidity >=0.6.0 <0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract UBNft is ERC721 {
    
    uint256 public tokenCounter;
    uint public maxLogos = 1;
    address owner;

    enum Logos{YOGESH}
    mapping(uint256 => Logos)  public tokenIdToLogo;
    mapping(uint256 => address)  public requestIdToSender;
    event requestLogo(uint256 indexed requestId , address owner);
    event logoAssigned(uint indexed tokenId , Logos logo);

    modifier OnlyOwner(){
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }
    constructor() public ERC721("Yogesh"){
        tokenCounter = 0;
        owner =  msg.sender;

    }


    function createLogoNFT(string memory _tokenURI ) public returns (uint256){
        require(tokenCounter < maxLogos , "Max number of logos minted");

        uint256 newTokenId = tokenCounter;

        requestIdToSender[newTokenId] = msg.sender;
        emit requestLogo(newTokenId, msg.sender);

        Logos logo = Logos(newTokenId);
        tokenIdToLogo(newTokenId)= msg.sender;

        emit logoAssigned(newTokenId, logo);
        tokenIdToLogo[newTokenId] = logo;

        _safeMint(msg.sender, newTokenId);
        _setTokenURI(newTokenId, _tokenURI);
        tokenCounter += 1;

        return newTokenId;
    }

}