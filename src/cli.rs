use clap::Parser;

use crate::theme;

#[derive(Parser)]
#[command(version, about, styles = theme::CLAP)]
pub struct Cli {}
