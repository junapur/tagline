use anstyle::{
    AnsiColor,
    Style,
};
use clap::builder::Styles;

pub const CLAP: Styles = Styles::plain()
    .header(AnsiColor::Blue.on_default().bold())
    .usage(AnsiColor::Blue.on_default().bold())
    .literal(Style::new().bold())
    .placeholder(Style::new().italic())
    .context(Style::new().dimmed())
    .context_value(Style::new())
    .error(AnsiColor::Red.on_default().bold())
    .invalid(AnsiColor::Red.on_default().bold())
    .valid(AnsiColor::Green.on_default().bold());
