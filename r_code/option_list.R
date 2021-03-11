option_list = list(
  make_option(c("--sanger"), default=NULL, type='character',
              help="enter the folder where the sanger data lives"),
  make_option(c("--freq), default=NULL, type='character',
              help="enter the folder where the NGS frequencies live"),

)
opt = parse_args(OptionParser(option_list=option_list))
