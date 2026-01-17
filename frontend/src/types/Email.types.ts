export interface EmailFormProps {
  emailText: string;
  setEmailText: (text: string) => void;
  onSubmit: () => void;
  isLoading: boolean;
  onClear: () => void;
}
