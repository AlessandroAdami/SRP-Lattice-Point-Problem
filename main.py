import os
import shutil
from manim import *

output_dir = "./media"

# Delete the folder of media you do not need
#if os.path.exists(output_dir): shutil.rmtree(output_dir)

class LPP(Scene):
    def construct(self):
        definition = Tex(
            r"This is a sentence"
        )
        definition.scale(0.8)
        self.play(Write(definition))
        self.wait(2)