import os
import comfy.sd
from nodes import recursive_search, filter_files_extensions, supported_pt_extensions

# VAEDecode
# VAELoader
# VAELoaderDecode

wd = os.getcwd()
print("working directory is ", wd)

filePath = __file__
print("This script file path is ", filePath)

absFilePath = os.path.abspath(__file__)
print("This script absolute path is ", absFilePath)

realFilePath = os.path.realpath(__file__)
print("This script real path is ", realFilePath)

path, filename = os.path.split(absFilePath)
print("Script file path is {}, filename is {}".format(path, filename))

class VAELoaderDecode:

    #models_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "models")
    models_dir = os.path.join(os.getcwd(),"ComfyUI", "models")
    vae_dir = os.path.join(models_dir, "vae")
    
    def __init__(self, device="cpu"):
        self.device = device
        print(f"VAELoaderDecode : {self.models_dir}")
    
    #@classmethod
    #def INPUT_TYPES(s):
    #    return {"required": { "samples": ("LATENT", ), "vae": ("VAE", )}}
    #    
    #@classmethod
    #def INPUT_TYPES(s):
    #    return {"required": { "vae_name": (filter_files_extensions(recursive_search(s.vae_dir), supported_pt_extensions), )}}
        
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": { 
                "samples": ("LATENT", ),
                "vae_name": (filter_files_extensions(recursive_search(s.vae_dir), supported_pt_extensions), )
            }
        }
        
    RETURN_TYPES = ("IMAGE",)
    
    FUNCTION = "test"

    CATEGORY = "latent"

    #TODO: scale factor?
    #def load_vae(self, vae_name):
    #    vae_path = os.path.join(self.vae_dir, vae_name)
    #    vae = comfy.sd.VAE(ckpt_path=vae_path)
    #    return (vae,)
    #    
    #def decode(self, vae, samples):
    #    return (vae.decode(samples["samples"]), )        
        
    def test(self, vae_name, samples):
        vae_path = os.path.join(self.vae_dir, vae_name)
        vae = comfy.sd.VAE(ckpt_path=vae_path)
        return (vae.decode(samples["samples"]), )
        
NODE_CLASS_MAPPINGS = {
    "VAELoaderDecode": VAELoaderDecode,
}