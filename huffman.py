import heapq
class BinaryTreeNode:
    def __init__(self,value,freq):
        self.left=None
        self.right=None
        self.value=value
        self.freq=freq
    def __lt__(self,other):
        return self.freq<other.freq
    def __eq__(self,other):
        return self.freq==other.freq
class Huffman_coding:
    def __init__(self,text):
        self.__text=text
        self.__minfreqheap=[]
        self.__codes={}
        
    ##step1:build freq dictionary     
    def __freq_dict(self):
        freq_dict={}
        for char in self.__text:
            if char  not in freq_dict:
                freq_dict[char]=1
            else:
                freq_dict[char]+=1
                
        return freq_dict  
    #step2:build heap of the frequencies in your text
    def __build_heap(self,freq_dict):
        for key in freq_dict:
            frequency=freq_dict[key]
            m=BinaryTreeNode(key,frequency)
            heapq.heappush(self.__minfreqheap,m)
            
            
    def __build_Binary_tree(self):
        while(len(self.__minfreqheap)>1):
            BinaryTreeNode1=heapq.heappop(self.__minfreqheap)
            BinaryTreeNode2=heapq.heappop(self.__minfreqheap)
            frequency=BinaryTreeNode1.freq+BinaryTreeNode2.freq
            BinaryTreeNode3=BinaryTreeNode(None,frequency)
            BinaryTreeNode3.left=BinaryTreeNode1
            BinaryTreeNode3.right=BinaryTreeNode2
            heapq.heappush(self.__minfreqheap,BinaryTreeNode3)
        return 
    def __build_codes_helper(self,root,curr_bits):
        if root is None:
            return
        
        if(root.value is not None):
            self.__codes[root.value]=curr_bits
        self.__build_codes_helper(root.left,"0"+curr_bits)
        self.__build_codes_helper(root.right,"1"+curr_bits)
    def __build_codes(self):
        root=heapq.heappop(self.__minfreqheap)
        st=""
        self.__build_codes_helper(root,st)
    def __encoded_text(self,text):
        st=""
        for char in text:
            st+=self.__codes[char]
        return st  
    def __padded_encoded_text(self,encoded):
        paded_amount=8-(len(encoded)%8)
        for i in range (paded_amount):
            encoded+='0'
        paded_info="{0:08b}".format(paded_amount)  
        encoded=paded_info+encoded
        return encoded
    def __getbytesarray(self,paded_encoded):
        array=[]
        for i in range(0,len(paded_encoded),8):
            bytes=paded_encoded[i:i+8]
            array.append(int(bytes,2))
        return array
             
    def compress(self):
        freq_dict={}
        
        freq_dict=self.__freq_dict()
        self.__build_heap(freq_dict)
        self.__build_Binary_tree()
        self.__build_codes()
        encoded=self.__encoded_text(text)
        paded_encoded=self.__padded_encoded_text(encoded)
        bytes_array=self.__getbytesarray(paded_encoded)
        final_bytes=bytes(bytes_array)
        print(paded_encoded)
      
        

text=input()
h=Huffman_coding(text)
h.compress()
