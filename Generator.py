class LLVMGenerator:
    def __init__(self):
        self.header = ""
        self.main = ""
        self.reg = 1
        self.str_i = 0
        self.br = 0
        self.brstack = []

    def printf_i32(self, id):
        self.main += f"%{self.reg} = load i32, i32* %{id}" + "\n"
        self.reg += 1
        self.main += f"%{self.reg} = call i32 (i8*, ...) @printf(i8* getelementptr " \
                     f"inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), " \
                     f"i32 %{self.reg - 1})" + "\n"
        self.reg+=1

    def printf_double(self, id):
        self.main += f"%{self.reg} = load double, double* %{id}" + "\n"
        self.reg += 1
        self.main += f"%{self.reg} = call i32 (i8*, ...) @printf(i8* getelementptr " \
                     f"inbounds ([4 x i8], [4 x i8]* @strpd, i32 0, i32 0), " \
                     f"double %{self.reg - 1})" + "\n"
        self.reg += 1

    def printf_string(self, text):
        str_len = len(text)
        str_type = f"[{str_len + 2} x i8]"
        self.header += f"@str{self.str_i} = constant {str_type} c\"{text}" + "\\0A\\00\"" + "\n"
        self.main += f"call i32 (i8*, ...) @printf(i8* getelementptr " \
                     f"inbounds ({str_type}, {str_type}* @str{self.str_i}, i32 0, i32 0))" + "\n"
        self.str_i += 1
        self.reg += 1

    def declare_i32(self, id):
        self.main += f"%{id} = alloca i32" + "\n"

    def declare_double(self, id):
        self.main += f"%{id} = alloca double" + "\n"

    def assign_i32(self, id, value):
        self.main += f"store i32 {value}, i32* %{id}" + "\n"

    def assign_double(self, id, value):
        self.main += f"store double {value}, double* %{id}" + "\n"

    def load_i32(self, id):
        self.main += f"%{self.reg} = load i32, i32* %{id}" + "\n"
        self.reg += 1

    def load_double(self, id):
        self.main += f"%{self.reg} = load double, double* %{id}" + "\n"
        self.reg += 1

    def add_i32(self, val1, val2):
        self.main += f"%{self.reg} = add i32 {val1}, {val2}" + "\n"
        self.reg += 1

    def add_double(self, val1, val2):
        self.main += f"%{self.reg} = fadd double {val1}, {val2}" + "\n"
        self.reg += 1

    def sub_i32(self, val1, val2):
        self.main += f"%{self.reg} = sub i32 {val1}, {val2}" + "\n"
        self.reg += 1

    def sub_double(self, val1, val2):
        self.main += f"%{self.reg} = fsub double {val1}, {val2}" + "\n"
        self.reg += 1

    def mult_i32(self, val1, val2):
        self.main += f"%{self.reg} = mul i32 {val1}, {val2}" + "\n"
        self.reg += 1

    def mult_double(self, val1, val2):
        self.main += f"%{self.reg} = fmul double {val1}, {val2}" + "\n"
        self.reg += 1

    def div_i32(self, val1, val2):
        self.main += f"%{self.reg} = sdiv i32 {val1}, {val2}" + "\n"
        self.reg += 1

    def div_double(self, val1, val2):
        self.main += f"%{self.reg} = fdiv double {val1}, {val2}" + "\n"
        self.reg += 1

    def sitofp(self, id):
        self.main += f"%{self.reg} = sitofp i32 %{id} to double" + "\n"
        self.reg += 1

    def fptosi(self, id):
        self.main += f"%{self.reg} = fptosi double %{id} to i32" + "\n"
        self.reg += 1

    def scanf_i32(self, id):
        self.main += f"%{self.reg} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr" \
                     f" inbounds ([3 x i8], [3 x i8]* @strs, i32 0, i32 0), i32* %{id})" + "\n"
        self.reg += 1

    def scanf_double(self, id):
        self.main += f"%{self.reg} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr " \
                     f"inbounds ([4 x i8], [4 x i8]* @strsd, i32 0, i32 0), double* %{id})" + "\n"
        ##self.assign_double(str(id), "%"+{self.reg})
        self.reg += 1

    def sqrt(self, value):
        self.main += f"%{self.reg} = call double @sqrt(double {value})" + "\n"
        self.reg += 1

    def icmp(self, id, value):
        self.main += f"%{self.reg} = load i32, i32* %{id}" + "\n"
        self.reg += 1
        self.main += f"%{self.reg} = icmp eq i32 %{self.reg - 1}, {value}" + "\n"
        self.reg += 1

    def icmp_lt(self, id, value):
        self.main += f"%{self.reg} = load i32, i32* %{id}" + "\n"
        self.reg += 1
        self.main += f"%{self.reg} = icmp slt i32 %{self.reg - 1}, {value}" + "\n"
        self.reg += 1

    def icmp_gt(self, id, value):
        self.main += f"%{self.reg} = load i32, i32* %{id}" + "\n"
        self.reg += 1
        self.main += f"%{self.reg} = icmp sgt i32 %{self.reg - 1}, {value}" + "\n"
        self.reg += 1

    def icmp_lte(self, id, value):
        self.main += f"%{self.reg} = load i32, i32* %{id}" + "\n"
        self.reg += 1
        self.main += f"%{self.reg} = icmp sle i32 %{self.reg - 1}, {value}" + "\n"
        self.reg += 1

    def icmp_gte(self, id, value):
        self.main += f"%{self.reg} = load i32, i32* %{id}" + "\n"
        self.reg += 1
        self.main += f"%{self.reg} = icmp sge i32 %{self.reg - 1}, {value}" + "\n"
        self.reg += 1

    def ifstart(self):
        self.br += 1
        self.main += f"br i1 %{self.reg - 1}, label %true {self.br}, label %false {self.br}" + "\n"
        self.main += f"true {self.br}" + ":\n"
        self.brstack.append(self.br)


    def ifend(self):
        b = self.brstack.pop()
        self.main += f"br label %false {b}" + "\n"
        self.main += f"false {b}" + ":\n"

    def repeatstart(self, repetitions):
        self.declare_i32(str(self.reg))
        counter = self.reg
        self.reg += 1
        self.assign_i32(str(counter), "0")
        self.br += 1
        self.main += f"br label %cond{self.br}" + "\n"
        self.main += f"cond{self.br}" + ":\n"
        self.load_i32(str(counter))
        self.add_i32(f"%{self.reg - 1}", "1")
        self.assign_i32(str(counter), f"%{self.reg - 1}")
        self.main += f"%{self.reg} = icmp slt i32 %{self.reg - 2}, {repetitions}" + "\n"
        self.reg += 1
        self.main += f"br i1 %{self.reg - 1}, label %true{self.br}, label %false{self.br}" + "\n"
        self.main += f"true{self.br}" + ":\n"
        self.brstack.append(self.br)

    def repeatend(self):
        b = self.brstack.pop()
        self.main += f"br label %cond{b}" + "\n"
        self.main += f"false{b}" + ":\n"


    def generate(self):
        text = ""
        text += "declare double @sqrt(double)\n"
        text += "declare i32 @printf(i8*, ...)\n"
        text += "declare i32 @__isoc99_scanf(i8*, ...)\n"
        text += "@strpi = constant [4 x i8] c\"%d\\0A\\00\"\n"
        text += "@strpd = constant [4 x i8] c\"%f\\0A\\00\"\n"
        text += "@strs = constant [3 x i8] c\"%d\\00\"\n"
        text += "@strsd = constant [4 x i8] c\"%lf\\00\"\n"
        text += self.header
        text += "define i32 @main() nounwind{\n"
        text += self.main
        text += "ret i32 0 }\n"
        return text
