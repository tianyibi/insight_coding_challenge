import sys

def generate_top_10_files(file_str, output_occ_str, output_state_str):
    # read file
    occ_dic = {}
    state_dic = {}
    total_certified = 0
    with open(file_str, 'r') as f:
        line1 = f.readline().rstrip('\n').split(';')
        # find index of SOC_NAME, SOC_CODE, CASE_STATUS, work state
        col_idx = [None for _ in range(4)]
        for idx, col in enumerate(line1):
            if "soc_name" in col.lower():
                col_idx[0] = idx
            elif "soc_code" in col.lower():
                col_idx[1] = idx
            elif "status" in col.lower():
                col_idx[2] = idx
            elif "state" in col.lower() and "work" in col.lower():
                col_idx[3] = idx

        if None in col_idx:
            raise ValueError("missing one of the SOC_NAME, SOC_CODE, CASE_STATUS or WORKSITE_STATE column")

        # go through file check status of each entry, save and count
        for line in f:
            entry = line.rstrip('\n').split(';')
            key = (entry[col_idx[1]])
            key_state = (entry[col_idx[3]])
            value_state = entry[col_idx[3]]
            value =  entry[col_idx[0]].strip('\"')

            if entry[col_idx[2]].lower() == "certified":
                total_certified += 1

                try:
                    occ_dic[key][0] -= 1
                except KeyError:
                    occ_dic[key] = [-1, value]

                try:
                    state_dic[key_state][0] -= 1
                except KeyError:
                    state_dic[key_state] = [-1, value_state]

    # sort occupation and state based on number of application and alphabetical order
    top_10_item = sorted(occ_dic.values())[:10] 
    top_10_state = sorted(state_dic.values())[:10]

    # write to 2 output files
    with open(output_occ_str, 'w') as f:
        f.write("TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")

        for item in top_10_item:
            f.write("{};{:d};{:.1f}%\n".format(item[1].upper(), -item[0], -item[0]*100/total_certified))

    with open(output_state_str, 'w') as f:
        f.write("TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")

        for state in top_10_state:
            f.write("{};{:d};{:.1f}%\n".format(state[1].upper(), -state[0], -state[0]*100/total_certified))
            
    return

if __name__ == "__main__":
    if len(sys.argv)-1 != 3:
        raise TypeError("Requires 3 arguments")
    generate_top_10_files(sys.argv[1], sys.argv[2], sys.argv[3])
