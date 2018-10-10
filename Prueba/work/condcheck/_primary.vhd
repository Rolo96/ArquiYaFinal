library verilog;
use verilog.vl_types.all;
entity condcheck is
    port(
        CondE           : in     vl_logic_vector(3 downto 0);
        Flags           : in     vl_logic_vector(3 downto 0);
        CondExE         : out    vl_logic
    );
end condcheck;
