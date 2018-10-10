library verilog;
use verilog.vl_types.all;
entity Execute is
    port(
        CLK             : in     vl_logic;
        RESET           : in     vl_logic;
        PCSrcE          : in     vl_logic;
        NoWrite         : in     vl_logic;
        RegWriteE       : in     vl_logic;
        MemWriteE       : in     vl_logic;
        BranchE         : in     vl_logic;
        ALUSrcE         : in     vl_logic;
        FlagsWriteE     : in     vl_logic_vector(1 downto 0);
        ForwardAE       : in     vl_logic_vector(1 downto 0);
        ForwardBE       : in     vl_logic_vector(1 downto 0);
        ALUControlE     : in     vl_logic_vector(3 downto 0);
        CondE           : in     vl_logic_vector(3 downto 0);
        FlagsE          : in     vl_logic_vector(3 downto 0);
        RD1E            : in     vl_logic_vector(31 downto 0);
        RD2E            : in     vl_logic_vector(31 downto 0);
        ExtImmE         : in     vl_logic_vector(31 downto 0);
        ResultW         : in     vl_logic_vector(31 downto 0);
        ALUResultM      : in     vl_logic_vector(31 downto 0);
        ALUFlagsEOut    : out    vl_logic_vector(3 downto 0);
        PCSrcEOut       : out    vl_logic;
        RegWriteEOut    : out    vl_logic;
        BranchEOut      : out    vl_logic;
        MemWriteEOut    : out    vl_logic;
        ALUResultE      : out    vl_logic_vector(31 downto 0);
        WriteDataE      : out    vl_logic_vector(31 downto 0)
    );
end Execute;
