import re

txt ="The rain in Spain"
x = re.findall("ai", txt)

txt_num = "abcs1231ok23ok12"
lst = re.findall(r"\d+", txt_num)

txt_space = "dang----quang-hung"
lst_space = re.search(r"\s", txt_space)
lst_name = re.split(r"-+", txt_space)
# if lst_space:
#     print(lst_space.start())

txt_special = "$12.85"

pattern = "\$(\d+\.\d+)"
lst_only_num = re.search(pattern, txt_special)

if lst_only_num:
    # print(lst_only_num.group(1))
    pass
else:
    print('Not found')

txt_check_sub = "dang  quang hung"

sub_func = re.sub(r"\s+", '0', txt_check_sub)
print(sub_func)