package fr.hyperfiction;


#if cpp
import cpp.Lib;
#elseif neko
import neko.Lib;
#end

import org.haxe.nme.HaxeObject;

/**
* ...
* @author shoe[box]
*/
/**
编译期执行的代码
*/
@:build( ShortCuts.mirrors( ) )
class HypSystem{

	/**
	* constructor
	*
	* @param
	* @return	void
	*/
	private function new() {

	}

	// -------o public

	/**
	*
	*
	* @public
	* @return	void
	*/
	#if android
	@JNI
	#end
	static public function isConnected( ) : Bool {
		return true;
	}

	/**
	*
	*
	* @public
	* @return	void
	*/

	#if android
	@JNI
	#end
	static public function isSmartPhone( ) : Bool {
		return false;
	}

	#if android
	@JNI
	#end
	static public function getUuid( ) : String {
		return "";
	}

	/**
	*
	*
	* @public
	* @return	void
	*/
	static public function dialog(
					sTitle		: String,
					sText		: String
					#if android	,
					?bCancelable	: Bool,
					?sNeg		: String ,
					?sPos		: String ,
					?fPos		: Void->Void,
					?fNeg		: Void->Void
					#end
					) : Void {
		#if android
		_show_error_dialog( sTitle , sText , bCancelable , sNeg , sPos , fPos , fNeg );
		#end
	}

	/**
	*
	*
	* @public
	* @return	void
	*/
	#if android
	@JNI
	#end
	static public function getSystem_lang( ) : String {
		var s = 'unknow';
		return s;
	}

	/**
	*
	*
	* @public
	* @return	void
	*/
	#if android
	@JNI
	#end
	static public function show_loading( bCancelable : Bool = true ) : Void {
	}

	/**
	*
	*
	* @public
	* @return	void
	*/
	#if android
	@JNI
	#end
	static public function hide_loading( ) : Void {
		#if blackberry
		hyp_hide_loading();
		#end
	}

	/**
	*
	*
	* @public
	* @return	void
	*/
	#if android
	@JNI
	#end
	static public function dismiss_loading( ) : Void {

	}

	/**
	*
	*
	* @private
	* @return	void
	*/
	static private function _show_error_dialog(
							sTitle		: String,
							sText		: String ,
							?bCancelable	: Bool,
							?sNeg		: String ,
							?sPos		: String ,
							?fPos		: Void->Void,
							?fNeg		: Void->Void
							) : Void{
		trace('_show_error_dialog ::: '+sText+" - "+sNeg+" - "+sPos);

		#if android
			if( sNeg == null && sPos == null )
				openDialog( sTitle , sText , bCancelable );
			else
				openCustomDialog( sTitle , sText , sNeg , sPos , new PopupCallBack( fPos , fNeg ));

		#end
	}

	/**
	*
	*
	* @private
	* @return	void
	*/
	#if android
	@JNI
	#end
	static private function openCustomDialog( sTitle : String , sText : String , sPos : String , sNeg : String , cb : HaxeObject ) : Void{
	}

	//Privates

	#if android
	@JNI
	#end
	private static function openDialog( sTitle : String , sText : String , bCancelable : Bool ) : Void{

	}

	/**
	*
	*
	* @public
	* @return	void
	*/
	#if android
	@JNI
	#end
	static public function setFixed_orientation( i : Int ) : Void {

	}

	/**
	*
	*
	* @public
	* @return	void
	*/
	#if android
	@JNI
	#end
	static public function reportError( sClass_name : String , sMessage : String , sStack : String ) : Void {

	}

	// -------o protected

	// -------o android

	//#if android

	/**
	*
	*
	* @public
	* @return	void
	*/
    #if android
	@JNI
    #end
	static public function isWifi( ) : Bool {
        return false;
	}

	/**
	*
	*
	* @public
	* @return	void
	*/
    #if android
	@JNI
    #end
	static public function getScreen_bucket( ) : String {
        return "";
	}

	/**
	*
	*
	* @public
	* @return	void
	*/
    #if android
	@JNI
    #end
	static public function getDensity( ) : String {
        return "";
	}

	/**
	*
	*
	* @public
	* @return	void
	*/
    #if android
	@JNI
    #end
	static public function wakeLock( iDelay : Int ) : Void {
    }

	/**
	*
	*
	* @public
	* @return	void
	*/
    #if android
	@JNI
    #end
	static public function keepScreen_on( ) : Void {
    }

	/**
	*
	*
	* @public
	* @return	void
	*/
    #if android
	@JNI
    #end
	static public function getLocal_IP( ) : String {
        return "127.0.0.1";
    }

	/**
	*
	*
	* @public
	* @return	void
	*/
    #if android
	@JNI
    #end
	static public function lightsOut( ) : Void {
    }

	//#end

	// -------o misc

}

#if android

/**
 * ...
 * @author shoe[box]
 */

class PopupCallBack extends HaxeObject{

	public var fPos : Void->Void;
	public var fNeg : Void->Void;

	// -------o constructor

	/**
	* constructor
	*
	* @param
	* @return	void
	*/
	public function new( fPos : Void->Void , fNeg : Void->Void ) {
		super( );
		this.fPos = fPos;
		this.fNeg = fNeg;
	}

	// -------o public

	/**
	*
	*
	* @public
	* @return	void
	*/
	public function pos( ) : Void {
		fPos( );
	}

	/**
	*
	*
	* @public
	* @return	void
	*/
	public function neg( ) : Void {
		fNeg( );
	}

	// -------o protected
	// -------o misc

}
#end
