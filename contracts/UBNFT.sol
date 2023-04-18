// SPDX-License-Identifier: MIT
pragma solidity >=0.6.0 <0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract UBNFT is ERC721 {
    
    uint256 public tokenCounter;
    uint public maxLogos = 1;
    address owner;

    enum Logos{YOGESH,ELECTION,POTRAIT}
    mapping(uint256 => Logos)  public tokenIdToLogo;
    mapping(uint256 => address)  public requestIdToSender;
    event requestLogo(uint256 indexed requestId , address owner);
    event logoAssigned(uint indexed tokenId , Logos logo);

 
    constructor() public ERC721("Yogesh","YogeshPic"){
        tokenCounter = 0;
        owner =  msg.sender;

    }


    function createLogoNFT(string memory _tokenURI ) public returns(uint256){

        uint256 newTokenId = tokenCounter;

        requestIdToSender[newTokenId] = msg.sender;
        emit requestLogo(newTokenId, msg.sender);

        Logos logo = Logos(newTokenId);
        tokenIdToLogo[newTokenId]= logo;
        emit logoAssigned(newTokenId, logo);
        _safeMint(msg.sender, newTokenId);
        _setTokenURI(newTokenId, _tokenURI);
        tokenCounter += 1;

        return newTokenId;
    }

}