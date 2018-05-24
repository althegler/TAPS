// Generated from Smeil.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link SmeilParser}.
 */
public interface SmeilListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link SmeilParser#module}.
	 * @param ctx the parse tree
	 */
	void enterModule(SmeilParser.ModuleContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmeilParser#module}.
	 * @param ctx the parse tree
	 */
	void exitModule(SmeilParser.ModuleContext ctx);
}