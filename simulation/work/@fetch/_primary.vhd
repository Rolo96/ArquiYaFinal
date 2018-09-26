library verilog;
use verilog.vl_types.all;
entity Fetch is
    generic(
        BITS            : integer := 32
    );
    port(
        ALUSResultE     : in     vl_logic_vector;
        ResultW         : in     vl_logic_vector;
        CLK             : in     vl_logic;
        PCSrcW          : in     vl_logic;
        BranchE         : in     vl_logic;
        StallF          : in     vl_logic;
        InstrF          : out    vl_logic_vector;
        PCPlus4F        : out    vl_logic_vector
    );
    attribute mti_svvh_generic_type : integer;
    attribute mti_svvh_generic_type of BITS : constant is 1;
end Fetch;
