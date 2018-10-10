library verilog;
use verilog.vl_types.all;
entity DataMemory is
    port(
        CLK             : in     vl_logic;
        WE              : in     vl_logic;
        A               : in     vl_logic_vector(31 downto 0);
        WD              : in     vl_logic_vector(31 downto 0);
        RD              : out    vl_logic_vector(31 downto 0)
    );
end DataMemory;
