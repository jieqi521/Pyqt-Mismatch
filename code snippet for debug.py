# 功能1：final_dict是一个字典，字典的value是dataframe，我们将 final_dict的内容导入到一个excel，sheetname就是字典的key，对应sheet里面的内容就是key对应的value(dataframe)

import pandas as pd
# 创建一个 ExcelWriter 对象
with pd.ExcelWriter('output.xlsx') as writer:
    # 遍历 final_dict 并将每个 DataFrame 写入对应的工作表
    for sheet_name, df in deep_clean_dict.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

# 
