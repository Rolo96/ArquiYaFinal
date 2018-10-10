library verilog;
use verilog.vl_types.all;
entity RegFile is
    port(
        clk             : in     vl_logic;
        reset           : in     vl_logic;
        we3             : in     vl_logic;
        a1              : in     vl_logic_vector(3 downto 0);
        a2              : in     vl_logic_vector(3 downto 0);
        wa3             : in     vl_logic_vector(3 downto 0);
        wd3             : in     vl_logic_vector(31 downto 0);
        r15             : in     vl_logic_vector(31 downto 0);
        rd1             : out    vl_logic_vector(31 downto 0);
        rd2             : out    vl_logic_vector(31 downto 0)
    );
end RegFile;
