
with open('sample.txt', 'r') as rf:
    with open('sample_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)
    
    
   

