library verilog;
use verilog.vl_types.all;
entity RegEM is
    port(
        CLK             : in     vl_logic;
        PCSrcECond      : in     vl_logic;
        RegWriteECond   : in     vl_logic;
        MemtoRegECond   : in     vl_logic;
        MemWriteECond   : in     vl_logic;
        ALUResultE      : in     vl_logic_vector(31 downto 0);
        WriteDataE      : in     vl_logic_vector(31 downto 0);
        WA3E            : in     vl_logic_vector(3 downto 0);
        PCSrcM          : out    vl_logic;
        RegWriteM       : out    vl_logic;
        MemtoRegM       : out    vl_logic;
        MemWriteM       : out    vl_logic;
        ALUResultM      : out    vl_logic_vector(31 downto 0);
        WriteDataM      : out    vl_logic_vector(31 downto 0);
        WA3M            : out    vl_logic_vector(3 downto 0)
    );
end RegEM;
