#ifndef HEADER.HPP
#define HEADER.HPP


class Lol{
	public:
		explicit Lol(int _a);
		~Lol();
		int get_some_smart_word() const;
		char* get_string() const;	


private:
		int some_smart_word = 15;
		char* string = nullptr;

};

#endif // HEADER.HPP
