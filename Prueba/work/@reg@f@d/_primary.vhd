library verilog;
use verilog.vl_types.all;
entity RegFD is
    generic(
        SIZE            : integer := 32
    );
    port(
        CLK             : in     vl_logic;
        StallD          : in     vl_logic;
        CLR             : in     vl_logic;
        RESET           : in     vl_logic;
        InstrF          : in     vl_logic_vector;
        InstrD          : out    vl_logic_vector
    );
    attribute mti_svvh_generic_type : integer;
    attribute mti_svvh_generic_type of SIZE : constant is 1;
end RegFD;
