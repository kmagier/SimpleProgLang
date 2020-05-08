class LLVMGenerator:
    def __init__(self):
        self.header = ""
        self.main = ""
        self.reg = 1

    def printf_i32(self, id):
        self.main += "%" + str(self.reg) + " = load i32, i32* %" + id + "\n";
        self.reg+=1
        self.main += "%" + str(self.reg) + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %" \
        + str(self.reg - 1) + ")\n"
        self.reg+=1

    def printf_double(self, id):
        self.main += "%" + str(self.reg) + " = load double, double* %" + id + "\n";
        self.reg+=1;
        self.main += "%" + str(self.reg) + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpd, i32 0, i32 0), double %" \
        + str(self.reg - 1) + ")\n";
        self.reg+=1

    def declare_i32(self, id):
        self.main += "%" + id + " = alloca i32\n"

    def declare_double(self, id):
        self.main += "%" + id + " = alloca double\n"

    def assign_i32(self, id, value):
        self.main += "store i32 " + value + ", i32* %" + id + "\n"

    def assign_double(self, id, value):
        self.main += "store double " + value + ", double* %" + id + "\n"

    def load_i32(self, id):
        self.main += "%" + str(self.reg) + " = load i32, i32* %" + id + "\n"
        self.reg += 1

    def load_double(self, id):
        self.main += "%" + str(self.reg) + " = load double, double* %" + id + "\n"
        self.reg +=1

    def add_i32(self, val1, val2):
        self.main += "%" + str(self.reg) + " = add i32 " + str(val1) + ", " + str(val2) + "\n"
        self.reg += 1

    def add_double(self, val1, val2):
        self.main += "%" + str(self.reg) + " = fadd double " + str(val1) + ", " + str(val2) + "\n"
        self.reg += 1

    def sub_i32(self, val1, val2):
        self.main += "%" + str(self.reg) + " = sub i32 " + str(val1) + ", " + str(val2) + "\n"
        self.reg += 1

    def sub_double(self, val1, val2):
        self.main += "%" + str(self.reg) + " = fsub double " + str(val1) + ", " + str(val2) + "\n"
        self.reg += 1

    def mult_i32(self, val1, val2):
        self.main += "%" + str(self.reg) + " = mul i32 " + str(val1) + ", " + str(val2) + "\n"
        self.reg +=1

    def mult_double(self, val1, val2):
        self.main += "%" + str(self.reg) + " = fmul double " + str(val1) + ", " + str(val2) + "\n"
        self.reg += 1

    def div_i32(self, val1, val2):
        self.main += "%" + str(self.reg) + " = sdiv i32 " + str(val1) + ", " + str(val2) + "\n"
        self.reg += 1

    def div_double(self, val1, val2):
        self.main += "%" + str(self.reg) + " =  fdiv double " + str(val1) + ", " + str(val2) + "\n"
        self.reg += 1

    def sitofp(self, id):
        self.main += "%" + str(self.reg) + " = sitofp i32 %" + id + " to double\n"
        self.reg += 1

    def fptosi(self, id):
        self.main += "%" + str(self.reg) + " = fptosi double " + id + " to i32\n"
        self.reg +=1

    def scanf_i32(self, id):
        self.main += "%" + str(self.reg) + " = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @strs, i32 0, i32 0), i32* %" + id + ")\n";
        self.reg += 1

    def scanf_double(self, id):
        self.main += "%" + str(self.reg) + " = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @strs, i32 0, i32 0), double* %" + id + ")\n";
        ##self.assign_double(str(id), "%"+str(self.reg))
        self.reg += 1

    def sqrt(self, id, value):
        self.main += "%" + id + " = call double @sqrt(double " + str(value) + ")\n"
        self.reg += 1



    def generate(self):
        text = ""
        text += "declare double @sqrt(double)\n"
        text += "declare i32 @printf(i8*, ...)\n"
        text += "declare i32 @__isoc99_scanf(i8*, ...)\n"
        text += "@strpi = constant [4 x i8] c\"%d\\0A\\00\"\n"
        text += "@strpd = constant [4 x i8] c\"%f\\0A\\00\"\n"
        text += "@strs = constant [3 x i8] c\"%d\\00\"\n"
        text += self.header
        text += "define i32 @main() nounwind{\n"
        text += self.main
        text += "ret i32 0 }\n"
        return text
