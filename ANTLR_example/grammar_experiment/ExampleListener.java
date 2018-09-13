// Generated from Example.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ExampleParser}.
 */
public interface ExampleListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ExampleParser#name}.
	 * @param ctx the parse tree
	 */
	void enterName(ExampleParser.NameContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExampleParser#name}.
	 * @param ctx the parse tree
	 */
	void exitName(ExampleParser.NameContext ctx);
}