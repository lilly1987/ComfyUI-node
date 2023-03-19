import os
import comfy.sd
from nodes import *
import folder_paths
import random
from custom_nodes.lilly_utills import *

print(os.getcwd())

class CheckpointLoaderSimpleText:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": { 
                "ckpt_name": (
                    "STRING", {
                        "multiline": False, 
                        "default": random.choice(folder_paths.get_filename_list("checkpoints"))
                    }
                ),
             }
         }
    RETURN_TYPES = ("MODEL", "CLIP", "VAE")
    FUNCTION = "load_checkpoint"

    CATEGORY = "loaders"
    
    def load_checkpoint(self, ckpt_name, output_vae=True, output_clip=True):
        ckpt_path =check_name_ckpt(name_split_choice(ckpt_name))
        if ckpt_path is None:
            print(f"{ckpt_name} is none")
            return 
        try:
            out = comfy.sd.load_checkpoint_guess_config(ckpt_path, output_vae=True, output_clip=True, embedding_directory=folder_paths.get_folder_paths("embeddings"))
            return out
        except Exception as e:
            print("CheckpointLoaderSimpleText Exception : "+ e)
            return 
            
        
NODE_CLASS_MAPPINGS = {
    "CheckpointLoaderSimpleText": CheckpointLoaderSimpleText,
}