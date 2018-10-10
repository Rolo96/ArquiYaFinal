library verilog;
use verilog.vl_types.all;
entity RegMW is
    generic(
        BITS            : integer := 32
    );
    port(
        ALUOutM         : in     vl_logic_vector;
        ReadDataM       : in     vl_logic_vector;
        PCSrcM          : in     vl_logic;
        RegWriteM       : in     vl_logic;
        MemtoRegM       : in     vl_logic;
        CLK             : in     vl_logic;
        RESET           : in     vl_logic;
        WA3M            : in     vl_logic_vector(3 downto 0);
        ALUOutW         : out    vl_logic_vector;
        ReadDataW       : out    vl_logic_vector;
        PCSrcW          : out    vl_logic;
        RegWriteW       : out    vl_logic;
        MemtoRegW       : out    vl_logic;
        WA3W            : out    vl_logic_vector(3 downto 0)
    );
    attribute mti_svvh_generic_type : integer;
    attribute mti_svvh_generic_type of BITS : constant is 1;
end RegMW;
