library verilog;
use verilog.vl_types.all;
entity RegPC is
    generic(
        BITS            : integer := 32
    );
    port(
        pcIn            : in     vl_logic_vector;
        stall           : in     vl_logic;
        CLK             : in     vl_logic;
        pcOut           : out    vl_logic_vector
    );
    attribute mti_svvh_generic_type : integer;
    attribute mti_svvh_generic_type of BITS : constant is 1;
end RegPC;
