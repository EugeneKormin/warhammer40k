class Prompt(object):
    def __init__(self):
        self.__prompts_that_divides_into_chunks: str

    @property
    def divide_into_chunks(self):
        return """
            Divide into paragraphs. Search for pronouns (like he, she, it, they and others) and replace them for whatever they actually means.
            
            Example: 
            'Mike is good at sports. He is a football player'. shall be changed to: 'Mike is good at sports. Mike is a football player' 
            
        """
