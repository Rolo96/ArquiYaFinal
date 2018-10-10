library verilog;
use verilog.vl_types.all;
entity CondUnit is
    port(
        CLK             : in     vl_logic;
        RESET           : in     vl_logic;
        PCSrcEIn        : in     vl_logic;
        RegWriteEIn     : in     vl_logic;
        MemWriteEIn     : in     vl_logic;
        BranchEIn       : in     vl_logic;
        NoWrite         : in     vl_logic;
        FlagWriteE      : in     vl_logic_vector(1 downto 0);
        CondE           : in     vl_logic_vector(3 downto 0);
        FlagsE          : in     vl_logic_vector(3 downto 0);
        ALUFlags        : in     vl_logic_vector(3 downto 0);
        ALUFlagsEOut    : out    vl_logic_vector(3 downto 0);
        PCSrcE          : out    vl_logic;
        RegWriteE       : out    vl_logic;
        BranchE         : out    vl_logic;
        MemWriteE       : out    vl_logic
    );
end CondUnit;
