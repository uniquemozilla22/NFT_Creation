import os
import json
from scripts.pinata import pinata_upload,get_pinned

def create_metadata():
    imgDir = '.\\images'
    metadatas = []

    pinnedFiles = get_pinned()

    for idx,file in enumerate(os.listdir(imgDir)):
        filepath = os.path.join(imgDir, file)
        logoName = file.split(".")[0]
        metadataFile = f'{logoName}.json'
        metadataFilepath = f'.\\Metadata\\{metadataFile}'

        if metadataFile in pinnedFiles:
              metadatas.append({"filename":metadataFile, "CID" :pinnedFiles[metadataFile] })
              continue

        result = pinata_upload(filepath)
        imgCID = result['IpfsHash']

        metadata = {
                "name": logoName,
                "description": f'Yogesh Picture logo: {logoName}',
                "image": imgCID,
                "attributes":
                  [
                          {"logo_size": idx * 2},
                          {"Powerlevel": idx}
                  ]
        }
        with open(metadataFilepath,"w") as f:
            json.dump(metadata,f)
        
        result = pinata_upload(metadataFilepath)
        metadatas.append({"filename":metadataFile, "CID": result["IpfsHash"]})
        
    return metadatas
    
if __name__ =='__main__':
    metadatas =  create_metadata()
    print(metadatas)