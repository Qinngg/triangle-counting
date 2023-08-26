# CXXFLAGS	= -march=native -O3
# CXXFLAGS	+= -std=c++11
# CXXFLAGS	+= -isystem ./include
# CXXFLAGS	+= -MMD
# CC	= g++

# TARGET	=  EvalLossLocal

# all: $(TARGET)

# EvalLossLocal: EvalLossLocal.o

# clean:
# 	rm -f *~ $(TARGET) *.d *.o

# -include *.d



CXXFLAGS	= -march=native -O3
CXXFLAGS	+= -std=c++11
CXXFLAGS	+= -isystem ./include
CXXFLAGS	+= -MMD
CXXFLAGS	+= -Xpreprocessor -fopenmp -lomp -I"/opt/homebrew/opt/libomp/include" -L"/opt/homebrew/opt/libomp/lib" #加入OpenMP标志

# 使用clang++作为编译器
CC	= clang++

TARGET	=  EvalLossLocal

all: $(TARGET)

EvalLossLocal: EvalLossLocal.o
	$(CC) $(CXXFLAGS) EvalLossLocal.o -o EvalLossLocal -lomp  # 链接OpenMP库

clean:
	rm -f *~ $(TARGET) *.d *.o

-include *.d
