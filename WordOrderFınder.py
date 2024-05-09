def Word_Order_Frequency_One_Book(Book, Word_Order, File_Output):
    with open(Book,'r',encoding="utf-8") as read_b:
        stopwords=['vol', 'fix', 'over', 'darent', 'so', 'put', 'f', 'whereby', 'off', 'primarily', 'have', 'former', 'obtain', 'related', 'sixty', 'tends', 'approximately', 'ought', 'date', 'there', 'briefly', 'whens', 'yours', 'five', 'twice', 'miss', 'same', 'keep', 'go', 'regarding', 'whatll', 'other', 'consider', 'whither', 'ive', 'ran', 'biol', 'seeming', 'third', 'thousand', 'always', 'thereupon', 'here', 'few', 'nor', 'around', 'system', 'whys', 'l', 'once', 'concerning', 'dare', 'shant', 'shell', 'came', 'me', 'com', 'being', 'noone', 'm', 'see', 'however', 'got', 'its', 'pages', 'successfully', 'ending', 'exactly', 'b', 'ill', 'on', 'trying', 'neither', 'reasonably', 'alone', 'where', 'ask', 'himself', 'hardly', 'instead', 'a', 'into', 'twenty', 'fifteen', 'at', 'somewhat', 'announce', 'until', 'used', 'fifty', 'looking', 'q', 'seems', 'u', 'itself', 'cs', 'ahead', 'thing', 'youve', 'may', 'everyone', 'saw', 'become', 'maynt', 'whole', 'meanwhile', 'shed', 'rather', 'herse', 'likely', 'quickly', 'tried', 'largely', 'in', 'corresponding', 'home', 'one', 'both', 'presumably', 'tip', 're', 'or', 'behind', 'now', 'heres', 'normally', 'wont', 'taking', 'knows', 'havent', 'several', 'follows', 'oughtnt', 'why', 'significantly', 'four', 'further', 'apart', 'youre', 'wants', 'less', 'hows', 'theyve', 'ever', 'etc', 'please', 'too', 'strongly', 'having', 'necessarily', 'example', 'should', 'greetings', 'each', 'during', 'bill', 'c', 'wholl', 'find', 'low', 'contain', 'shouldnt', 'then', 'of', 'describe', 'k', 'zero', 'onto', 'lets', 'herself', 'when', 'nowhere', 'did', 'consequently', 'amid', 'whereupon', 'important', 'therell', 'thereof', 'usefulness', 'appropriate', 'plus', 'specified', 'refs', 'ts', 'toward', 'thin', 'followed', 'except', 'past', 'inc', 'keeps', 'afterwards', 'cant', 'empty', 'whereafter', 'page', 'anybody', 'might', 'backwards', 'itll', 'does', 'especially', 'aside', 'werent', 'notwithstanding', 'downwards', 'front', 'doing', 'if', 'yourself', 'ltd', 'which', 'thoroughly', 'seriously', 'nd', 'quite', 'right', 'inward', 'though', 'allows', 'your', 'unless', 'regardless', 'hadnt', 'before', 'hundred', 'directly', 'saying', 'thats', 'but', 'possibly', 'better', 'best', 'usefully', 'thick', 'am', 'along', 'by', 'amongst', 'whom', 'necessary', 'whod', 'her', 'thou', 'hence', 'states', 'importance', 'recent', 'giving', 'nearly', 'g', 'and', 'ok', 'couldnt', 'they', 'thus', 'fewer', 'means', 'eg', 'inc.', 'my', 'hither', 'it', 'little', 'serious', 'beginnings', 'rd', 'against', 'down', 'million', 'very', 'comes', 'use', 'becoming', 'throughout', 'half', 'run', 'widely', 'round', 'lest', 'potentially', 'y', 'merely', 'wonder', 'be', 'via', 's', 'fifth', 'allow', 'although', 'specify', 'poorly', 'much', 'formerly', 'ours', 'selves', 'anyways', 'almost', 'could', 'seem', 'them', 'help', 'im', 'amidst', 'whereas', 'up', 'top', 'begins', 'hes', 'p', 'cause', 'somehow', 'words', 'research', 'gotten', 'detail', 'whoever', 'how', 'act', 'moreover', 'who', 'wasnt', 'hopefully', 'move', 'particularly', 'already', 'unto', 'que', 'shows', 'somebody', 'suggest', 'nobody', 'anymore', 'ignored', 'wherever', 'proud', 'mr', 'some', 'someone', 'h', 'nay', 't', 'respectively', 'results', 'was', 'thence', 'says', 'near', 'everywhere', 'seen', 'unfortunately', 'qv', 'thereto', 'him', 'mightnt', 'going', 'nonetheless', 'believe', 'abst', 'happens', 'hid', 'call', 'asking', 'outside', 'hed', 'didnt', 'isnt', 'ref', 'n', 'becomes', 'course', 'six', 'different', 'side', 'nine', 'hell', 'owing', 'possible', 'first', 'gone', 'among', 'wouldnt', 'most', 'kept', 'o', 'seemed', 'beside', 'overall', 'amount', 'name', 'come', 'showns', 'nos', 'everybody', 'still', 'whim', 'invention', 'effect', 'itd', 'relatively', 'thereve', 'opposite', 'contains', 'neverf', 'thatve', 'somewhere', 'to', 'th', 'thoughh', 'interest', 'give', 'make', 'affects', 'ninety', 'sec', 'lately', 'made', 'whilst', 'ca', 'e', 'according', 'changes', 'eighty', 'con', 'yes', 'therere', 'associated', 'no', 'getting', 'again', 'way', 'know', 'tell', 'hereby', 'apparently', 'wish', 'want', 'ex', 'ff', 'dont', 'accordingly', 'cmon', 'stop', 'yet', 'the', 'actually', 'noted', 'anyhow', 'taken', 'theyd', 'ml', 'despite', 'things', 'next', 'say', 'aren', 'inner', 'three', 'likewise', 'fill', 'km', 'our', 'anywhere', 'sufficiently', 'thanx', 'uucp', 'lower', 'said', 'goes', 'minus', 'due', 'forty', 'co.', 'sometime', 'an', 'as', 'readily', 'let', 'aint', 'thank', 'others', 'than', 'looks', 'arent', 'vols', 'awfully', 'such', 'w', 'for', 'hasnt', 'himse', 'arise', 'inside', 'described', 'between', 'sent', 'thereafter', 'neverless', 'enough', 'above', 'someday', 'many', 'fairly', 'v', 'twelve', 'far', 'sincere', 'while', 'shown', 'nevertheless', 'all', 'nothing', 'think', 'end', 'indicate', 'appreciate', 'something', 'perhaps', 'hereafter', 'with', 'yourselves', 'pp', 'indeed', 'caption', 'mainly', 'whats', 'mill', 'is', 'useful', 'gave', 've', 'herein', 'hereupon', 'promptly', 'welcome', 'edu', 'resulted', 'forever', 'else', 'ten', 'hello', 'i', 'hi', 'till', 'immediately', 'shes', 'na', 'more', 'www', 'd', 'away', 'ed', 'must', 'took', 'insofar', 'truly', 'provided', 'together', 'adopted', 'self', 'themselves', 'myse”', 'recently', 'per', 'mostly', 'became', 'affected', 'latter', 'mean', 'til', 'whatve', 'sometimes', 'currently', 'own', 'vs', 'cannot', 'z', 'under', 'howbeit', 'look', 'meantime', 'towards', 'x', 'anyway', 'are', 'she', 'any', 'upon', 'begin', 'cry', 'wherein', 'thirty', 'therefore', 'mg', 'showed', 'whenever', 'really', 'whatever', 'thatll', 'theyll', 'these', 'furthermore', 'resulting', 'eight', 'specifying', 'available', 'thereby', 'everything', 'would', 'since', 'sup', 'causes', 'every', 'another', 'specifically', 'et', 'present', 'mustnt', 'co', 'uses', 'theirs', 'not', 'sensible', 'ah', 'particular', 'viz', 'section', 'within', 'ago', 'thru', 'll', 'take', 'anyone', 'doesnt', 'do', 'eleven', 'containing', 'seeing', 'auth', 'below', 'ie', 'significant', 'shall', 'that', 'myself', 'beyond', 'hers', 'un', 'through', 'about', 'following', 'either', 'secondly', 'maybe', 'wheres', 'ourselves', 'done', 'need', 'went', 'okay', 'whence', 'r', 'value', 'substantially', 'obviously', 'certain', 'second', 'throug', 'only', 'known', 'somethan', 'thorough', 'were', 'he', 'their', 'after', 'from', 'line', 'placed', 'predominantly', 'without', 'makes', 'later', 'ups', 'usually', 'etal', 'similarly', 'will', 'alongside', 'mrs', 'whichever', 'try', 'old', 'entirely', 'backward', 'sure', 'beginning', 'found', 'non', 'new', 'index', 'can', 'mug', 'across', 'well', 'also', 'this', 'beforehand', 'whose', 'thered', 'out', 'farther', 'therein', 'neednt', 'mine', 'had', 'versus', 'given', 'affecting', 'show', 'otherwise', 'indicates', 'gets', 'weve', 'inasmuch', 'besides', 'you', 'back', 'whether', 'previously', 'needs', 'omitted', 'similar', 'latterly', 'whomever', 'brief', 'been', 'state', 'considering', 'sub', 'forth', 'least', 'novel', 'elsewhere', 'anything', 'even', 'willing', 'tries', 'gives', 'computer', 'various', 'whos', 'part', 'slightly', 'unlikely', 'ord', 'two', 'able', 'using', 'us', 'fire', 'theyre', 'j', 'added', 'sorry', 'underneath', 'obtained', 'theres', 'provides', 'youd', 'soon', 'what', 'definitely', 'his', 'accordance', 'id', 'kg', 'abroad', 'has', 'like', 'namely', 'none', 'get', 'full', 'ones', 'immediate', 'I', 'thanks', 'indicated', 'because', 'itse”', 'probably', 'unlike', 'clearly', 'keys', 'we', 'oh', 'forward', 'last', 'seven', 'just', 'undoing', 'world', 'youll', 'often', 'liked', 'wed', 'adj', 'certainly', 'regards', 'never', 'appear', 'information', 'evermore', 'de', 'upwards', 'bottom', 'those']
        
        readbook= read_b.readlines()
        str_book= " ".join(readbook)
        book_rplc=str_book.replace(","," ").replace(";", " ").replace("."," ").replace(":"," ")
        book_rplc=book_rplc.replace("!"," ").replace("#"," ").replace("^"," ").replace("\n","").replace('\'','')  
        book_rplc=book_rplc.replace("..."," ").replace("$"," ").replace("€"," ").replace("%"," ").replace("&"," ")
        book_rplc=book_rplc.replace("/", " ").replace("{"," ").replace("}"," ").replace("("," ").replace(")"," ")
        book_rplc=book_rplc.replace("["," ").replace("]"," ").replace("="," ").replace("*"," ").replace("+"," ")
        book_rplc=book_rplc.replace("?"," ").replace("-"," ").replace("_"," ").replace("\""," ")
        book_rplc= book_rplc.replace("0", " ").replace("1", " ").replace("2", " ").replace("3", " ").replace("4", " ")
        book_rplc= book_rplc.replace("6", " ").replace("7", " ").replace("8", " ").replace("9", " ").replace("5", " ")
        lowercase_book=book_rplc.lower()
        book_list= lowercase_book.split()
        
        booklist=[]
        for word in book_list:
            if word not in stopwords:
                booklist.append(word)  
            
                
        dictionary={}
        with open(File_Output,'w',encoding="utf-8") as out:
            if Word_Order==1:
               
               for word in booklist:
                   if word in dictionary:
                       dictionary[word] +=1
                   else:
                       dictionary[word]=1
                                               
               out.writelines("| WORD               | WORD               |\n")   
               out.writelines("| ORDER              | ORDER              |\n")   
               out.writelines("| FREQUENCY          | SEQUENCE           |\n")   
               out.writelines("-------------------------------------------\n")   

               for k,v in dictionary.items():
                   out.writelines(f"{v}                  |     {k} \n")
                 
            elif Word_Order==2:
                for i in range(len(booklist)-1):
                    word=""
                    word= booklist[i] + " "+ booklist[i+1]
                    if word in dictionary:
                        dictionary[word] +=1
                    else:
                        dictionary[word]=1
                    
                out.writelines("| WORD               | WORD               |\n")   
                out.writelines("| ORDER              | ORDER              |\n")   
                out.writelines("| FREQUENCY          | SEQUENCE           |\n")   
                out.writelines("-------------------------------------------\n")   

                for k,v in dictionary.items():
                    out.writelines(f"{v}                  |     {k} \n")
                  
                
            else:
                print("Word_Order is not valid. ")  
        
           


def Word_Order_Frequency_Two_Books(Book_1, Book_2, Word_Order, File_Output):
    with open(Book_1,'r',encoding="utf-8") as read_1:
        with open(Book_2,'r',encoding="utf-8") as read_2:
            stopwords=['vol', 'fix', 'over', 'darent', 'so', 'put', 'f', 'whereby', 'off', 'primarily', 'have', 'former', 'obtain', 'related', 'sixty', 'tends', 'approximately', 'ought', 'date', 'there', 'briefly', 'whens', 'yours', 'five', 'twice', 'miss', 'same', 'keep', 'go', 'regarding', 'whatll', 'other', 'consider', 'whither', 'ive', 'ran', 'biol', 'seeming', 'third', 'thousand', 'always', 'thereupon', 'here', 'few', 'nor', 'around', 'system', 'whys', 'l', 'once', 'concerning', 'dare', 'shant', 'shell', 'came', 'me', 'com', 'being', 'noone', 'm', 'see', 'however', 'got', 'its', 'pages', 'successfully', 'ending', 'exactly', 'b', 'ill', 'on', 'trying', 'neither', 'reasonably', 'alone', 'where', 'ask', 'himself', 'hardly', 'instead', 'a', 'into', 'twenty', 'fifteen', 'at', 'somewhat', 'announce', 'until', 'used', 'fifty', 'looking', 'q', 'seems', 'u', 'itself', 'cs', 'ahead', 'thing', 'youve', 'may', 'everyone', 'saw', 'become', 'maynt', 'whole', 'meanwhile', 'shed', 'rather', 'herse', 'likely', 'quickly', 'tried', 'largely', 'in', 'corresponding', 'home', 'one', 'both', 'presumably', 'tip', 're', 'or', 'behind', 'now', 'heres', 'normally', 'wont', 'taking', 'knows', 'havent', 'several', 'follows', 'oughtnt', 'why', 'significantly', 'four', 'further', 'apart', 'youre', 'wants', 'less', 'hows', 'theyve', 'ever', 'etc', 'please', 'too', 'strongly', 'having', 'necessarily', 'example', 'should', 'greetings', 'each', 'during', 'bill', 'c', 'wholl', 'find', 'low', 'contain', 'shouldnt', 'then', 'of', 'describe', 'k', 'zero', 'onto', 'lets', 'herself', 'when', 'nowhere', 'did', 'consequently', 'amid', 'whereupon', 'important', 'therell', 'thereof', 'usefulness', 'appropriate', 'plus', 'specified', 'refs', 'ts', 'toward', 'thin', 'followed', 'except', 'past', 'inc', 'keeps', 'afterwards', 'cant', 'empty', 'whereafter', 'page', 'anybody', 'might', 'backwards', 'itll', 'does', 'especially', 'aside', 'werent', 'notwithstanding', 'downwards', 'front', 'doing', 'if', 'yourself', 'ltd', 'which', 'thoroughly', 'seriously', 'nd', 'quite', 'right', 'inward', 'though', 'allows', 'your', 'unless', 'regardless', 'hadnt', 'before', 'hundred', 'directly', 'saying', 'thats', 'but', 'possibly', 'better', 'best', 'usefully', 'thick', 'am', 'along', 'by', 'amongst', 'whom', 'necessary', 'whod', 'her', 'thou', 'hence', 'states', 'importance', 'recent', 'giving', 'nearly', 'g', 'and', 'ok', 'couldnt', 'they', 'thus', 'fewer', 'means', 'eg', 'inc.', 'my', 'hither', 'it', 'little', 'serious', 'beginnings', 'rd', 'against', 'down', 'million', 'very', 'comes', 'use', 'becoming', 'throughout', 'half', 'run', 'widely', 'round', 'lest', 'potentially', 'y', 'merely', 'wonder', 'be', 'via', 's', 'fifth', 'allow', 'although', 'specify', 'poorly', 'much', 'formerly', 'ours', 'selves', 'anyways', 'almost', 'could', 'seem', 'them', 'help', 'im', 'amidst', 'whereas', 'up', 'top', 'begins', 'hes', 'p', 'cause', 'somehow', 'words', 'research', 'gotten', 'detail', 'whoever', 'how', 'act', 'moreover', 'who', 'wasnt', 'hopefully', 'move', 'particularly', 'already', 'unto', 'que', 'shows', 'somebody', 'suggest', 'nobody', 'anymore', 'ignored', 'wherever', 'proud', 'mr', 'some', 'someone', 'h', 'nay', 't', 'respectively', 'results', 'was', 'thence', 'says', 'near', 'everywhere', 'seen', 'unfortunately', 'qv', 'thereto', 'him', 'mightnt', 'going', 'nonetheless', 'believe', 'abst', 'happens', 'hid', 'call', 'asking', 'outside', 'hed', 'didnt', 'isnt', 'ref', 'n', 'becomes', 'course', 'six', 'different', 'side', 'nine', 'hell', 'owing', 'possible', 'first', 'gone', 'among', 'wouldnt', 'most', 'kept', 'o', 'seemed', 'beside', 'overall', 'amount', 'name', 'come', 'showns', 'nos', 'everybody', 'still', 'whim', 'invention', 'effect', 'itd', 'relatively', 'thereve', 'opposite', 'contains', 'neverf', 'thatve', 'somewhere', 'to', 'th', 'thoughh', 'interest', 'give', 'make', 'affects', 'ninety', 'sec', 'lately', 'made', 'whilst', 'ca', 'e', 'according', 'changes', 'eighty', 'con', 'yes', 'therere', 'associated', 'no', 'getting', 'again', 'way', 'know', 'tell', 'hereby', 'apparently', 'wish', 'want', 'ex', 'ff', 'dont', 'accordingly', 'cmon', 'stop', 'yet', 'the', 'actually', 'noted', 'anyhow', 'taken', 'theyd', 'ml', 'despite', 'things', 'next', 'say', 'aren', 'inner', 'three', 'likewise', 'fill', 'km', 'our', 'anywhere', 'sufficiently', 'thanx', 'uucp', 'lower', 'said', 'goes', 'minus', 'due', 'forty', 'co.', 'sometime', 'an', 'as', 'readily', 'let', 'aint', 'thank', 'others', 'than', 'looks', 'arent', 'vols', 'awfully', 'such', 'w', 'for', 'hasnt', 'himse', 'arise', 'inside', 'described', 'between', 'sent', 'thereafter', 'neverless', 'enough', 'above', 'someday', 'many', 'fairly', 'v', 'twelve', 'far', 'sincere', 'while', 'shown', 'nevertheless', 'all', 'nothing', 'think', 'end', 'indicate', 'appreciate', 'something', 'perhaps', 'hereafter', 'with', 'yourselves', 'pp', 'indeed', 'caption', 'mainly', 'whats', 'mill', 'is', 'useful', 'gave', 've', 'herein', 'hereupon', 'promptly', 'welcome', 'edu', 'resulted', 'forever', 'else', 'ten', 'hello', 'i', 'hi', 'till', 'immediately', 'shes', 'na', 'more', 'www', 'd', 'away', 'ed', 'must', 'took', 'insofar', 'truly', 'provided', 'together', 'adopted', 'self', 'themselves', 'myse”', 'recently', 'per', 'mostly', 'became', 'affected', 'latter', 'mean', 'til', 'whatve', 'sometimes', 'currently', 'own', 'vs', 'cannot', 'z', 'under', 'howbeit', 'look', 'meantime', 'towards', 'x', 'anyway', 'are', 'she', 'any', 'upon', 'begin', 'cry', 'wherein', 'thirty', 'therefore', 'mg', 'showed', 'whenever', 'really', 'whatever', 'thatll', 'theyll', 'these', 'furthermore', 'resulting', 'eight', 'specifying', 'available', 'thereby', 'everything', 'would', 'since', 'sup', 'causes', 'every', 'another', 'specifically', 'et', 'present', 'mustnt', 'co', 'uses', 'theirs', 'not', 'sensible', 'ah', 'particular', 'viz', 'section', 'within', 'ago', 'thru', 'll', 'take', 'anyone', 'doesnt', 'do', 'eleven', 'containing', 'seeing', 'auth', 'below', 'ie', 'significant', 'shall', 'that', 'myself', 'beyond', 'hers', 'un', 'through', 'about', 'following', 'either', 'secondly', 'maybe', 'wheres', 'ourselves', 'done', 'need', 'went', 'okay', 'whence', 'r', 'value', 'substantially', 'obviously', 'certain', 'second', 'throug', 'only', 'known', 'somethan', 'thorough', 'were', 'he', 'their', 'after', 'from', 'line', 'placed', 'predominantly', 'without', 'makes', 'later', 'ups', 'usually', 'etal', 'similarly', 'will', 'alongside', 'mrs', 'whichever', 'try', 'old', 'entirely', 'backward', 'sure', 'beginning', 'found', 'non', 'new', 'index', 'can', 'mug', 'across', 'well', 'also', 'this', 'beforehand', 'whose', 'thered', 'out', 'farther', 'therein', 'neednt', 'mine', 'had', 'versus', 'given', 'affecting', 'show', 'otherwise', 'indicates', 'gets', 'weve', 'inasmuch', 'besides', 'you', 'back', 'whether', 'previously', 'needs', 'omitted', 'similar', 'latterly', 'whomever', 'brief', 'been', 'state', 'considering', 'sub', 'forth', 'least', 'novel', 'elsewhere', 'anything', 'even', 'willing', 'tries', 'gives', 'computer', 'various', 'whos', 'part', 'slightly', 'unlikely', 'ord', 'two', 'able', 'using', 'us', 'fire', 'theyre', 'j', 'added', 'sorry', 'underneath', 'obtained', 'theres', 'provides', 'youd', 'soon', 'what', 'definitely', 'his', 'accordance', 'id', 'kg', 'abroad', 'has', 'like', 'namely', 'none', 'get', 'full', 'ones', 'immediate', 'I', 'thanks', 'indicated', 'because', 'itse”', 'probably', 'unlike', 'clearly', 'keys', 'we', 'oh', 'forward', 'last', 'seven', 'just', 'undoing', 'world', 'youll', 'often', 'liked', 'wed', 'adj', 'certainly', 'regards', 'never', 'appear', 'information', 'evermore', 'de', 'upwards', 'bottom', 'those']
            
            readbook1= read_1.readlines()
            str_book1= " ".join(readbook1)
            book_rplc1=str_book1.replace(","," ").replace(";", " ").replace("."," ").replace(":"," ")
            book_rplc1=book_rplc1.replace("!"," ").replace("#"," ").replace("^"," ").replace("\n","").replace('\'','')  
            book_rplc1=book_rplc1.replace("..."," ").replace("$"," ").replace("€"," ").replace("%"," ").replace("&"," ")
            book_rplc1=book_rplc1.replace("/", " ").replace("{"," ").replace("}"," ").replace("("," ").replace(")"," ")
            book_rplc1=book_rplc1.replace("["," ").replace("]"," ").replace("="," ").replace("*"," ").replace("+"," ")
            book_rplc1=book_rplc1.replace("?"," ").replace("-"," ").replace("_"," ").replace("\""," ")
            book_rplc1= book_rplc1.replace("0", " ").replace("1", " ").replace("2", " ").replace("3", " ").replace("4", " ")
            book_rplc1= book_rplc1.replace("6", " ").replace("7", " ").replace("8", " ").replace("9", " ").replace("5", " ")
            lowercase_book1=book_rplc1.lower()
            book_list1= lowercase_book1.split()
            
            booklist1=[]
            for word1 in book_list1:
                if word1 not in stopwords:
                    booklist1.append(word1)  
                 
                    
           
            readbook2= read_2.readlines()
            str_book2= " ".join(readbook2)
            book_rplc2=str_book2.replace(","," ").replace(";", " ").replace("."," ").replace(":"," ")
            book_rplc2=book_rplc2.replace("!"," ").replace("#"," ").replace("^"," ").replace("\n","").replace('\'','')  
            book_rplc2=book_rplc2.replace("..."," ").replace("$"," ").replace("€"," ").replace("%"," ").replace("&"," ")
            book_rplc2=book_rplc2.replace("/", " ").replace("{"," ").replace("}"," ").replace("("," ").replace(")"," ")
            book_rplc2=book_rplc2.replace("["," ").replace("]"," ").replace("="," ").replace("*"," ").replace("+"," ")
            book_rplc2=book_rplc2.replace("?"," ").replace("-"," ").replace("_"," ").replace("\""," ")
            book_rplc2= book_rplc2.replace("0", " ").replace("1", " ").replace("2", " ").replace("3", " ").replace("4", " ")
            book_rplc2= book_rplc2.replace("6", " ").replace("7", " ").replace("8", " ").replace("9", " ").replace("5", " ")
            lowercase_book2=book_rplc2.lower()
            book_list2= lowercase_book2.split()
            
            booklist2=[]
            for word2 in book_list2:
                if word2 not in stopwords:
                    booklist2.append(word2)  
            
            dictionary1={}                     
            dictionary2={}
               
            with open(File_Output,'w',encoding="utf-8") as out: 
                if Word_Order==1:
                    for word1 in booklist1:
                        if word1 in dictionary1:
                            dictionary1[word1] +=1
                        else:
                            dictionary1[word1]=1
                            
                    for word2 in booklist2:
                        if word2 in dictionary2:
                            dictionary2[word2] +=1
                        else:
                            dictionary2[word2]=1  
                                        
                    out.writelines("| TOTAL           | BOOK 1              | BOOK 2              | WORD               |\n")   
                    out.writelines("| ORDER           | ORDER               | ORDER               | ORDER              | \n")   
                    out.writelines("| FREQUENCY       | FREQUENCY           | FREQUENCY           | SEQUENCE           |\n")   
                    out.writelines("------------------------------------------------------------------------------------\n")  
                    for k1,v1 in dictionary1.items():
                        for k2,v2 in dictionary2.items():
                            if k1==k2:                    
                                out.writelines(f"|{int(v1)+int(v2)}                 |{v1}                    |{v2}                    |{k2}             |\n")
                                out.writelines("-----------------------------------------------------------------------------------------\n")  
                                break         
                elif Word_Order==2:
                    for i in range(len(booklist1)-1):
                        word1=""
                        word1= booklist1[i] + " "+ booklist1[i+1]
                        if word1 in dictionary1:
                            dictionary1[word1] +=1
                        else:
                            dictionary1[word1]=1
                            
                    for j in range(len(booklist2)-1):
                        word2=""
                        word2= booklist2[j] + " "+ booklist2[j+1]
                        if word2 in dictionary2:
                            dictionary2[word2] +=1
                        else:
                            dictionary2[word2]=1     
                            
                    out.writelines("| TOTAL           | BOOK 1              | BOOK 2              | WORD               |\n")   
                    out.writelines("| ORDER           | ORDER               | ORDER               | ORDER              | \n")   
                    out.writelines("| FREQUENCY       | FREQUENCY           | FREQUENCY           | SEQUENCE           |\n")   
                    out.writelines("------------------------------------------------------------------------------------\n")  
                    for k1,v1 in dictionary1.items():
                        for k2,v2 in dictionary2.items():
                            if k1==k2:                    
                                out.writelines(f"|{int(v1)+int(v2)}                 |{v1}                    |{v2}                    |{k1}             |\n")
                                out.writelines("-----------------------------------------------------------------------------------------\n")  
                                break          
                            
                else:
                       print("Word_Order is not valid. ")  
                                  
                       
                


