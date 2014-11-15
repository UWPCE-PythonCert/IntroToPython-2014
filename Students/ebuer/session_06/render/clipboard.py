    def render(self, file_out, ind=""):

        self.file_out = file_out.write(u'{indent}<{tag}>\n'
            .format(indent=self.indent, tag=Element.tag))

        for line in self.content:  # render each line from list
            self.file_out = file_out.write(u'{indent}{content}\n'
                .format(indent=self.indent+ind, content=line))

        self.file_out = file_out.write(u'{indent}</{tag}>\n'
            .format(indent=self.indent, tag=Element.tag))



        Body.render(self, file_out, ind=ind*2)
        P.render(self, file_out, ind=ind*3)
