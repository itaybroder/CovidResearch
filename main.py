import pandas as pd
import numpy as np
import os

from netchop import create_dataframe, feed_to_Netchop
from MHCpan import split_for_all_peptides
from config import HOME_DIRECTORY, INPUT_DIR, OUTPUT_DIR, PATH_TO_NETCHOP


#choose you can choose the RNA either from here or through the .fasta file
mutent_dict = {
   'seq1' : 'MFVFLVLLPLVSSQCVNLTTRTQLPPAYTNSFTRGVYYPDKVFRSSVLHSTQDLFLPFFSNVTWFHAIHVSGTNGTKRFDNPVLPFNDGVYFASTEKSNIIRGWIFGTTLDSKTQSLLIVNNATNVVIKVCEFQFCNDPFLGVYYHKNNKSWMESEFRVYSSANNCTFEYVSQPFLMDLEGKQGNFKNLREFVFKNIDGYFKIYSKHTPINLVRDLPQGFSALEPLVDLPIGINITRFQTLLALHRSYLTPGDSSSGWTAGAAAYYVGYLQPRTFLLKYNENGTITDAVDCALDPLSETKCTLKSFTVEKGIYQTSNFRVQPTESIVRFPNITNLCPFGEVFNATRFASVYAWNRKRISNCVADYSVLYNSASFSTFKCYGVSPTKLNDLCFTNVYADSFVIRGDEVRQIAPGQTGKIADYNYKLPDDFTGCVIAWNSNNLDSKVGGNYNYLYRLFRKSNLKPFERDISTEIYQAGSTPCNGVEGFNCYFPLQSYGFQPTNGVGYQPYRVVVLSFELLHAPATVCGPKKSTNLVKNKCVNFNFNGLTGTGVLTESNKKFLPFQQFGRDIADTTDAVRDPQTLEILDITPCSFGGVSVITPGTNTSNQVAVLYQDVNCTEVPVAIHADQLTPTWRVYSTGSNVFQTRAGCLIGAEHVNNSYECDIPIGAGICASYQTQTNSPRRARSVASQSIIAYTMSLGAENSVAYSNNSIAIPTNFTISVTTEILPVSMTKTSVDCTMYICGDSTECSNLLLQYGSFCTQLNRALTGIAVEQDKNTQEVFAQVKQIYKTPPIKDFGGFNFSQILPDPSKPSKRSFIEDLLFNKVTLADAGFIKQYGDCLGDIAARDLICAQKFNGLTVLPPLLTDEMIAQYTSALLAGTITSGWTFGAGAALQIPFAMQMAYRFNGIGVTQNVLYENQKLIANQFNSAIGKIQDSLSSTASALGKLQDVVNQNAQALNTLVKQLSSNFGAISSVLNDILSRLDKVEAEVQIDRLITGRLQSLQTYVTQQLIRAAEIRASANLAATKMSECVLGQSKRVDFCGKGYHLMSFPQSAPHGVVFLHVTYVPAQEKNFTTAPAICHDGKAHFPREGVFVSNGTHWFVTQRNFYEPQIITTDNTFVSGNCDVVIGIVNNTVYDPLQPELDSFKEELDKYFKNHTSPDVDLGDISGINASVVNIQKEIDRLNEVAKNLNESLIDLQELGKYEQYIKWPWYIWLGFIAGLIAIVMVTIMLCCMTSCCSCLKGCCSCGSCCKFDEDDSEPVLKGVKLHYT',
   'seq2': 'MFVFLVLLPLVSSQCVNLTTRTQLPPAYTNSFTRGVYYPDKVFRSSVLFDTQDLFLPFFSNVTWFHAIHVSGTNGTKRDFNPVLPFNDGVYFASTEKSNIIRGWIFGTTLDSKTQSLLIVNNATNVVIKVCEFQFCNDPFLGVYYHKNNKSWMESEFRVYSSANNCTFEYVSQPFLMDLEGKQGNFKNLREFVFKNIDGYFKIYSKHTPINLVRDLPQGFSALEPLVDLPIGINITRFQTLLALHRSYLTPGDSSSGWTAGAAAYYVGYLQPRTFLLKYNENGTITDAVDCALDPLSETKCTLKSFTVEKGIYQTSNFRVQPTESIVRFPNITNLCPFGEVFNATRFASVYAWNRKRISNCVADYSVLYNSASFSTFKCYGVSPTKLNDLCFTNVYADSFVIRGDEVRQIAPGQTGKIADYNYKLPDDFTGCVIAWNSNNLDSKVGGNYNYLYRLFRKSNLKPFERDISTEIYQAGSTPCNGVEGFNCYFPLQSYGFQPTNGVGYQPYRVVVLSFELLHAPATVCGPKKSTNLVKNKCVNFNFNGLTGTGVLTESNKKFLPFQQFGRDIADTTDAVRDPQTLEILDITPCSFGGVSVITPGTNTSNQVAVLYQDVNCTEVPVAIHADQLTPTWRVYSTGSNVFQTRAGCLIGAEHVNNSYECDIPIGAGICASYQTQTNSPRRARSVASQSIIAYTMSLGAENSVAYSNNSIAIPTNFTISVTTEILPVSMTKTSVDCTMYICGDSTECSNLLLQYGSFCTQLNRALTGIAVEQDKNTQEVFAQVKQIYKTPPIKDFGGFNFSQILPDPSKPSKRSFIEDLLFNKVTLADAGFIKQYGDCLGDIAARDLICAQKFNGLTVLPPLLTDEMIAQYTSALLAGTITSGWTFGAGAALQIPFAMQMAYRFNGIGVTQNVLYENQKLIANQFNSAIGKIQDSLSSTASALGKLQDVVNQNAQALNTLVKQLSSNFGAISSVLNDILSRLDKVEAEVQIDRLITGRLQSLQTYVTQQLIRAAEIRASANLAATKMSECVLGQSKRVDFCGKGYHLMSFPQSAPHGVVFLHVTYVPAQEKNFTTAPAICHDGKAHFPREGVFVSNGTHWFVTQRNFYEPQIITTDNTFVSGNCDVVIGIVNNTVYDPLQPELDSFKEELDKYFKNHTSPDVDLGDISGINASVVNIQKEIDRLNEVAKNLNESLIDLQELGKYEQFDFFYIKWPWYIWLGFIAGLIAIVMVTIMLCCMTSCCSCLKGCCSCGSCCKFDEDDSEPVLKGVKLHYT'
}
if(not os.path.isdir(INPUT_DIR)):
    os.mkdir(INPUT_DIR)

if(not os.path.isdir(OUTPUT_DIR)):
    os.mkdir(OUTPUT_DIR)

input_file = open(INPUT_DIR+"/spike.fasta", "w")
for i in mutent_dict:
  input_file.write(">" + i)
  input_file.write("\n")
  input_file.write(mutent_dict[i])
  input_file.write("\n")
input_file.close()


def cystine(pep):
    for i in range(1, len(pep)-2):
         print(pep)
        if(pep[i] == "C"):
           
            return True
    return False

def netchop_mutation_pipeline(mutation_dict):  
    #creating all peptides from RNA
    a1 = split_for_all_peptides(mutent_dict['seq1'])

    #creating a dataframe with all the peptides and positions and adding a "choped" column
    cols1 = ['peptide', 'start_pos','end_pos']
    df1 =  pd.DataFrame(a1, columns=cols1)
    df1["Chopped"] = ''
    a2 = split_for_all_peptides(mutent_dict['seq2'])
    cols2 = ['peptide_after_mutation', 'start_pos_after_mutation','end_pos_mutation']
    df2 =  pd.DataFrame(a2, columns=cols1)
    df2['Chopped'] = ''

    #add choped indicator to the df
    input_file = INPUT_DIR +"/spike.fasta"
    output_file = OUTPUT_DIR + "/out.txt"
    feed_to_Netchop(input_file, output_file, PATH_TO_NETCHOP)
    df1 = create_dataframe(output_file, df1, 'seq1', OUTPUT_DIR)
    df2 = create_dataframe(output_file, df2, 'seq2', OUTPUT_DIR)
    
    result = df1
    df1["cysteine"] = np.where(cystine(df1["peptide"]), True, False)

    # result = df1.merge(df2, how='left', left_on=['start_pos', 'end_pos'], right_on=['start_pos','end_pos'], suffixes=['_before_mutation', '_after_mutation'])
    return result
    
result = netchop_mutation_pipeline(mutent_dict)
result.to_csv(OUTPUT_DIR + "/result.csv")