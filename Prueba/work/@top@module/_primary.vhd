library verilog;
use verilog.vl_types.all;
entity TopModule is
    generic(
        BITS            : integer := 32
    );
    port(
        CLK             : in     vl_logic;
        RESET           : in     vl_logic
    );
    attribute mti_svvh_generic_type : integer;
    attribute mti_svvh_generic_type of BITS : constant is 1;
end TopModule;
