library(optparse)

WDIR = getwd()
#gets the working dir

option_list = list(
  make_option(c("--sanger"), default=NULL, type='character',
              help="enter the folder where the sanger data lives"),
  make_option(c("--freq), default=NULL, type='character',
              help="enter the folder where the NGS frequencies live"),
  make_option(c("outfile"), default=NULL,
              help="Enter intended name of output csv file")

)
opt = parse_args(OptionParser(option_list=option_list))

sanger <- paste0(WDIR, opt$sanger)
