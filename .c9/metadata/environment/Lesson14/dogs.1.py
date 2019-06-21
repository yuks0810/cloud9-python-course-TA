{"filter":false,"title":"dogs.1.py","tooltip":"/Lesson14/dogs.1.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":34,"column":43},"action":"remove","lines":["class Dog:","      voice = \"国によって変わる\"","      ","      def __init__(self, name):","            self.name = name","      ","      def bark(self):","            print(self.voice)","            ","      @classmethod","      def description(self):","            print(F\"世界の犬の鳴き声は{self.voice}\")","            ","class English_Dog(Dog):","      #property（クラスメンバ変数）","      voice = \"bow!\"","      ","      #constructor（インスタンスメンバ変数）","      def __init__(self, name = \"Buddy\"):","            super().__init__(name)","","      #class method","      @classmethod","      def description(self):","            print(f\"英語圏の犬の鳴き声は{self.voice}\")","            ","class Japanese_Dog(Dog):","      voice = \"ワン！\"","      ","      def __init__(self, name = \"ポチ\"):","            super().__init__(name)","","      @classmethod","      def description(self):","            print(f\"日本の犬の鳴き声は{self.voice}\")"],"id":2},{"start":{"row":0,"column":0},"end":{"row":26,"column":30},"action":"insert","lines":["class Dog:","    country = \"世界\"","    voice = \"国によって変わる\"","    ","    def __init__(self, name):","        self.name = name","    ","    def bark(self):","        print(self.voice)","","    @classmethod","    def description(self):","        print(f\"{self.country}の犬の鳴き声は{self.voice}\")","","class English_Dog(Dog):","    country = \"英語圏\"","    voice = \"bow!\"","    ","    def __init__(self, name = \"Buddy\"):","        super().__init__(name)","","class Japanese_Dog(Dog):","    country = \"日本\"","    voice = \"ワン！\"","    ","    def __init__(self, name = \"ポチ\"):","        super().__init__(name)"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":4,"column":13},"end":{"row":4,"column":14},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1554103229154,"hash":"056b2bad1ec985589447d66c2dc91ccbb08053bc"}