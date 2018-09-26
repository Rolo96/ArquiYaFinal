library verilog;
use verilog.vl_types.all;
entity RegEM is
    generic(
        BITS            : integer := 32
    );
    port(
        ALUResultE      : in     vl_logic_vector;
        WriteDataE      : in     vl_logic_vector;
        PCSrcE          : in     vl_logic;
        RegWriteE       : in     vl_logic;
        MemtoRegE       : in     vl_logic;
        MemWriteE       : in     vl_logic;
        CLK             : in     vl_logic;
        WA3E            : in     vl_logic_vector(3 downto 0);
        ALUResultM      : out    vl_logic_vector;
        WriteDataM      : out    vl_logic_vector;
        PCSrcM          : out    vl_logic;
        RegWriteM       : out    vl_logic;
        MemtoRegM       : out    vl_logic;
        MemWriteM       : out    vl_logic;
        WA3M            : out    vl_logic_vector(3 downto 0)
    );
    attribute mti_svvh_generic_type : integer;
    attribute mti_svvh_generic_type of BITS : constant is 1;
end RegEM;
